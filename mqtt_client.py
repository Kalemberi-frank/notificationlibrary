# iot_notification_system/mqtt_client.py
import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, broker="broker.hivemq.com"):
        self.client = mqtt.Client()
        self.client.connect(broker, 1883, 60)

    def send_message(self, topic, message):
        """Send a message to the specified MQTT topic."""
        self.client.publish(topic, message)
