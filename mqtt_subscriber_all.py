import paho.mqtt.client as mqtt
from datetime import datetime
MQTT_SERVER = "localhost"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Temp(P)")
    client.subscribe("Humidity(P)")
    client.subscribe("Pressure(P)")
    client.subscribe("Temp(A)")
    client.subscribe("Humidity(A)")
    client.subscribe("Pressure(A)")
    client.subscribe("Temp(B)")
    client.subscribe("Humidity(B)")
    client.subscribe("Pressure(B)")
    client.subscribe("Temp(C)")
    client.subscribe("Humidity(C)")
    client.subscribe("Pressure(C)")
    client.subscribe("Temp(D)")
    client.subscribe("Humidity(D)")
    client.subscribe("Pressure(D)")
    client.subscribe("Temp(E)")
    client.subscribe("Humidity(E)")
    client.subscribe("Pressure(E)")
    client.subscribe("Temp(F)")
    client.subscribe("Humidity(F)")
    client.subscribe("Pressure(F)")
    client.subscribe("Temp(G)")
    client.subscribe("Humidity(G)")
    client.subscribe("Pressure(G)")
    client.subscribe("Temp(H)")
    client.subscribe("Humidity(H)")
    client.subscribe("Pressure(H)")
    client.subscribe("Temp(I)")
    client.subscribe("Humidity(I)")
    client.subscribe("Pressure(I)")
    client.subscribe("Temp(J)")
    client.subscribe("Humidity(J)")
    client.subscribe("Pressure(J)")
    client.subscribe("Temp(R)")
    client.subscribe("Humidity(R)")
    client.subscribe("Pressure(R)")
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # (P) denotes Purple sensor working. 
    if msg.topic == "Temp(A)" or "Pressure(A)" or "Humidity(A)":
        file1=open("DataLog(A).txt","a")
        if msg.topic == "Temp(A)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(A)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(A)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
            
    if msg.topic == "Temp(B)" or "Pressure(B)" or "Humidity(B)":
        file1=open("DataLog(B).txt","a")
        if msg.topic == "Temp(B)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(B)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(B)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
            
    if msg.topic == "Temp(C)" or "Pressure(C)" or "Humidity(C)":
        file1=open("DataLog(C).txt","a")
        if msg.topic == "Temp(C)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(C)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(C)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
            
    if msg.topic == "Temp(D)" or "Pressure(D)" or "Humidity(D)":
        file1=open("DataLog(D).txt","a")
        if msg.topic == "Temp(D)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(D)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(D)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
            
    if msg.topic == "Temp(E)" or "Pressure(E)" or "Humidity(E)":
        file1=open("DataLog(E).txt","a")
        if msg.topic == "Temp(E)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(E)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(E)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
            
    if msg.topic == "Temp(F)" or "Pressure(F)" or "Humidity(F)":
        file1=open("DataLog(F).txt","a")
        if msg.topic == "Temp(F)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(F)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(F)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
            
    if msg.topic == "Temp(G)" or "Pressure(G)" or "Humidity(G)":
        file1=open("DataLog(G).txt","a")
        if msg.topic == "Temp(G)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(G)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(G)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
            
    if msg.topic == "Temp(H)" or "Pressure(H)" or "Humidity(H)":
        file1=open("DataLog(H).txt","a")
        if msg.topic == "Temp(H)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(H)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(H)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
            
    if msg.topic == "Temp(I)" or "Pressure(I)" or "Humidity(I)":
        file1=open("DataLog(I).txt","a")
        if msg.topic == "Temp(I)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(I)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(I)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
            
    if msg.topic == "Temp(J)" or "Pressure(J)" or "Humidity(J)":
        file1=open("DataLog(J).txt","a")
        if msg.topic == "Temp(J)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(J)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(J)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
            
            
    if msg.topic == "Temp(R)" or "Pressure(R)" or "Humidity(R)":
        file1=open("DataLog(R).txt","a")
        if msg.topic == "Temp(R)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(R)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(R)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
        
    if msg.topic == "Temp(P)" or "Pressure(P)" or "Humidity(P)":
        file1=open("DataLog(P).txt","a")
        if msg.topic == "Temp(P)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(P)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(P)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)
"""
def on_disconnect(client, userdata,rc):
    current.time = stamp_to_time(time.time
    logging.info("disconnecting reason " + str(rc))
    client.connected_flag=False
    client.disconnect_flag=True
"""
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
