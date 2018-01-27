import paho.mqtt.client as mqtt
import time
import requests

# Network configuration
mqtt_broker_address = "130.211.134.220"
mqtt_broker_port = 1883

scoring_server_address = "http://localhost:80"
scoring_server_port = 8080

# Instantiate Mosquitto client
client = mqtt.Client("P1")
client.connect(mqtt_broker_address, port=mqtt_broker_port)


# Mosquitto callbacks
def on_log(client, userdata, level, buf):
    print("log: ", buf)


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    response = requests.post(scoring_server_address + '/score', json={'image': '1bc324cf8cb'})
    print(response.status_code, response.reason)
    client.publish("coverage-hackathon-resp", response.status_code)
    print(response.json())


# Start Mosquitto loop
client.loop_start()
client.subscribe("coverage-hackathon")
client.on_message = on_message
client.on_log = on_log


client.publish("coverage-hackathon", "OFF")


time.sleep(4)
client.loop_stop()

