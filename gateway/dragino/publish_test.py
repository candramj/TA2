import paho.mqtt.client as paho
import time
from random import seed
from random import random

def on_publish(client, userdata, mid):
    print("message dikirim: "+str(mid))
def read_location():
    return random()
 
client = paho.Client()
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

while True:
    fo=open("lokasi.txt", "r+")
    lokasi=fo.read(21);
    
    (rc, mid) = client.publish("lokasi/", str(lokasi), qos=1)
    print(lokasi)
    time.sleep(5)
