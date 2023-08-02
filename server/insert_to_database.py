import paho.mqtt.client as paho
import mysql.connector

def on_subscribe(client, userdata, mid, granted_qos):
        print ("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        node=str(msg.payload)[2]
        latitude=str(msg.payload)[4:12]
        longitude=str(msg.payload)[13:23]

        if node is not None and node != '' and latitude is not None and latitude      != '' and longitude is not None and longitude != '':
                print("node= "+node+"\n")
                print("latitude= "+latitude+"\n")
                print("longitude= "+longitude+"\n")
                mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="MyNewPass",
                        database="lora"
                        )
                mycursor = mydb.cursor()


                sql = "INSERT INTO location (id, latitude, longitude) VALUES (%s     , %s, %s)"
                val = [node, latitude, longitude]
                mycursor.execute(sql, val)
                mydb.commit()

                print(mycursor.rowcount, "was inserted.")

client=paho.Client()
client.on_subscribe=on_subscribe
client.on_message=on_message
client.connect("broker.mqttdashboard.com", 1883)
client.subscribe("lokasi/", qos=1)

client.loop_forever()
