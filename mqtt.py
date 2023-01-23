import json
import paho.mqtt.client as mqtt
import requests

host = "test.mosquitto.org"
cms_url = "http://cms.quitiweb.com"
# cms_url = "http://127.0.0.1:8000"
token = r"qEukfbNJ70Waitk2AvycmtfP?xel-9/pwps6iRSQ"


def on_connect(local_client, userdata, flags, rc):
    print('------------------------------')
    print("Connected with result code", rc)
    # local_client.subscribe("$SYS/#")
    # local_client.subscribe("$SYS/grifos/login")
    local_client.subscribe(topic='grifos/#', qos=2)


def on_message(local_client, userdata, message):
    # print(message.topic, message.payload)
    print('------------------------------')
    msg = str(message.payload.decode("utf-8"))

    print('topic: {}'.format(message.topic))
    print('payload: {}'.format(message.payload))
    print('qos: {}'.format(message.qos))

    mac = ""
    response = {}
    res_json = ""

    if "mac" in msg and "version" in msg:
        print("LOGIN COMMAND")
        payload_json = json.loads(msg)
        mac = payload_json['mac']

        response = requests.get(
            cms_url + "/api/login",
            params={"mac": mac}
        )

    elif "GetDate" in msg:
        print("GetDate COMMAND")

    elif "GetPlaylist" in msg:
        print("GetPlaylist COMMAND")
        topic_str = str(message.topic)
        mac = topic_str.split("/")[1]

        response = requests.get(
            cms_url + "/api/get_playlist",
            params={"mac": mac}
        )
    else:
        return

    if response:
        res_json = response.json()

    local_client.publish(
        topic="grifos/{}".format(mac),
        payload=str(res_json)
    )


# client = mqtt.Client(
#     client_id="", clean_session=True, userdata=None,
#     protocol=mqtt.MQTTv311, transport="tcp"
# )

client = mqtt.Client(client_id="grifo_cms", clean_session=False)
client.on_connect = on_connect
client.on_message = on_message

# client.username_pw_set(USER, PASS)
# client.tls_set()
# client.connect(host, 9101, 10)
# client.connect(host=host, posrt=1883, keepalive=60)
client.connect(host=host, port=1883)

# client.loop_start()
client.loop_forever()
