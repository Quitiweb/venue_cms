import paho.mqtt.client as mqtt

host = 'test.mosquitto.org'


def on_connect(local_client, userdata, rc):
    print("Connected with result code", rc)
    # local_client.subscribe("$SYS/#")
    # local_client.subscribe("$SYS/grifos/login")
    local_client.subscribe(topic='grifos/login', qos=2)


def on_message(local_client, userdata, message):
    print(message.topic, message.payload)
    print('------------------------------')
    print('topic: %s' % message.topic)
    print('payload: %s' % message.payload)
    print('qos: %d' % message.qos)
    # if str(message.payload).find('CMD') != -1


# client = mqtt.Client(
#     client_id="", clean_session=True, userdata=None,
#     protocol=mqtt.MQTTv311, transport="tcp"
# )

client = mqtt.Client(client_id="grifo_cms", clean_session=False)
client.on_connect = on_connect
client.on_message = on_message

# client = mqtt.Client("mqtt-test")  # client ID "mqtt-test"
# client.on_connect = on_connect
# client.on_message = on_message
# client.username_pw_set(USER, PASS)
# client.connect('127.0.0.1', 1883)

# client.connect("test.mosquitto.org", 1883, 60)
client.tls_set()
# client.connect(host, 9101, 10)
client.connect(host=host, port=1883, keepalive=60)
print(client)
print(client.on_connect)
print(client.on_message)

# client.connect("test.mosquitto.org/#/", 1883, 60)
# client.loop_start()
client.loop_forever()
