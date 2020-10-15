#!/usr/bin/env /home/mpiima/rifdata/readings/bin/python
import paho.mqtt.client as mqtt
import json
import format

def connectivity():
    response = os.system("ping -c 2 facebook.com")
    if response == 0:
        pass
    else:
        connectivity()
connectivity()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    strrg = str(msg.payload)
    format.writeCsv(strrg)
    #print(msg.topic+" "+strrg)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("katanga", password="ttn-account-v2.l5Cfo5by3jTYT7zh1ZxFtfAI3_OsbVM7jmWEPtSuPvs")

client.connect("eu.thethings.network")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
