import paho.mqtt.client as mqtt
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
 print("Connected with result code "+str(rc))
 client.subscribe("/test/1") # Topic /test/1 을 구독한다.
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
 print(msg.topic+" "+str(msg.payload))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host = "3.38.162.214") # — 브로커 IP 주소
client.loop_forever()