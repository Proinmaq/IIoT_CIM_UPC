import time
import paho.mqtt.client as mqtt

# Constants
PORT_MQTT = 1883

BROKER = "192.168.100.53"
TOPIC_ON = "MQTT/ON"
TOPIC_OFF = "MQTT/OFF"

active = True

mqttc = mqtt.Client()

def on_connect(mqttc, obj, flags, rc):
    print("rc: {}".format(rc))
    mqttc.subscribe("MQTT/ON")
    mqttc.subscribe("MQTT/OFF")

def on_disconnect(mqttc, obj, flags, rc):
    print("Reconnecting to MQTT Broker at {} {} ...".format(BROKER, PORT_MQTT))
    mqttc.connect(BROKER, PORT_MQTT, 60)
    
def on_publish(mqttc, obj, mid):
    print("mid: {}".format(mid))

def on_message(client, userdata, msg):
    global active
    print('New message recieved -> topic:{} - payload:{}'.format(msg.topic, msg.payload))
    if msg.topic == "MQTT/ON":
        if msg.payload == b'ON':
            active = True;
       
    elif msg.topic == "MQTT/OFF":
        if msg.payload == b'OFF':
            active = False
    print("active = {}".format(active))

mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.on_message = on_message

mqttc.connect(BROKER, PORT_MQTT, 60)

mqttc.loop_start()

while True:
    print("[INFO] The sate of variable {}".format(active))
    time.sleep(2.0)

