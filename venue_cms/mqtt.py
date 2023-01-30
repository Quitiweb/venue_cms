import json
import paho.mqtt.client as mqtt
import requests

host = "test.mosquitto.org"
cms_url = "http://cms.quitiweb.com"


def on_connect(local_client, userdata, flags, rc):
    print('------------------------------')
    print("Connected with result code", rc)
    local_client.subscribe(topic='grifos/#', qos=2)


def on_message(local_client, userdata, message):
    print('------------------------------')
    msg = str(message.payload.decode("utf-8"))

    print('topic: {}'.format(message.topic))
    print('payload: {}'.format(message.payload))
    print('qos: {}'.format(message.qos))

    mac = ""
    response = {}
    res_json = ""

    if "mac" in msg and "version" in msg:
        print("Login COMMAND")
        payload_json = json.loads(msg)
        mac = payload_json['mac']

        response = requests.get(
            cms_url + "/api/login",
            params={"mac": mac}
        )

    elif "GetDate" in msg:
        print("GetDate COMMAND")
        payload_json = json.loads(msg)
        token = payload_json['token']

        response = requests.get(
            cms_url + "/api/get_date",
            params={"token": token}
        )

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


client = mqtt.Client(client_id="grifo_cms", clean_session=False)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host=host, port=1883)
