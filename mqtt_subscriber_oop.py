import paho.mqtt.client as mqtt
from datetime import datetime
MQTT_SERVER = "localhost"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    pi_list = ["P", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "R"]
    for i in pi_list:
        try:
            client.subscribe("Temp({})".format(i))
            client.subscribe("Humidity({})".format(i))
            client.subscribe("Pressure({})".format(i))
        except:
            pass


def on_message(client, userdata, msg):
    # (P) denotes Purple sensor working.
    pi_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "R", "P"]
    for i in pi_list:
        try:
            if msg.topic == "Temp({})".format(i) or "Pressure({})".format(
                    i) or "Humidity({})".format(i):
                file1 = open("DataLog({}).txt".format(i), "a")
                if msg.topic == "Temp({})".format(i):
                    now = datetime.now()
                    dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
                    file1.write(dt_string)
                    file1.write(msg.payload)
                    print(dt_string)
                    print(msg.topic + "     " + str(msg.payload))
                if msg.topic == "Pressure({})".format(i):
                    file1.write(" " + msg.payload)
                    print(msg.topic + " " + str(msg.payload))
                if msg.topic == "Humidity({})".format(i):
                    file1.write(" " + msg.payload)
                    print(msg.topic + " " + str(msg.payload))
                    file1.write('\n')
        except:
            pass


"""
on_message:
    1) read from all Pis
    2) read all T,P,H,t variables
    3) write to corresponding .txt file
    NEW:
    4) after reading T,P,H,t, we are going to check for violation
    5) if violation:
        a) send email and text
    6) implement some debouncing scheme
"""


def on_disconnect(client, userdata, rc):
    # current.time = stamp_to_time(time.time)
    # logging.info("disconnecting reason " + str(rc))
    client.connected_flag = False
    client.disconnect_flag = True


if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_SERVER, 1883, 60)
    client.on_disconnect = on_disconnect
    client.loop_forever()
