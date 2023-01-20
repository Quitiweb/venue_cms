import paho.mqtt.client as mqtt


IP = '51.77.150.39'
USER = 'debian'
PASS = 'vxPm23ftT9wg'


def on_connect(local_client, userdata, rc):
    local_client.subscribe("$SYS/#")


def on_message(local_client, userdata, msg):
    # Do something
    pass


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# client = mqtt.Client("mqtt-test")  # client ID "mqtt-test"
# client.on_connect = on_connect
# client.on_message = on_message
# client.username_pw_set(USER, PASS)
# client.connect('127.0.0.1', 1883)

# client.connect("test.mosquitto.org", 1883, 60)
client.tls_set()
client.username_pw_set(USER, PASS)
# client.connect(IP, 9101, 10)
client.connect(host=IP, port=1883, keepalive=60)
print(client)
print(client.on_connect)
print(client.on_message)

# client.connect("test.mosquitto.org/#/", 1883, 60)
# client.loop_start()
# client.loop_forever()
