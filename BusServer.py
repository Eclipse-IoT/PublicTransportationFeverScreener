# Copyright (c) 2021 Eclipse Foundation.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0.
#
# SPDX-License-Identifier: EPL-2.0
#
# Original Author: Joongho Kim

import paho.mqtt.client as mqtt
import time


MQTT_BROKER = "172.31.0.74"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Temperature")
    client.subscribe("Fever")
    client.subscribe("Transaction")
    client.subscribe("Occupancy")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
        

    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("windows", "windows")

client.connect(MQTT_BROKER, 1883)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
