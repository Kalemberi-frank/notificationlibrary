# iot_notification_system/notifier.py
import logging
import paho.mqtt.client as mqtt

class NotificationSystem:
    def __init__(self, mqtt_broker="broker.hivemq.com"):
        self.client = mqtt.Client()
        self.client.connect(mqtt_broker, 1883, 60)
        self.logger = logging.getLogger("NotificationSystem")
        logging.basicConfig(filename='app.log', level=logging.WARNING)

    def send_notification(self, topic, message):
        """Publish message to the given MQTT topic."""
        self.client.publish(topic, message)
        self.logger.warning(f"Notification sent to {topic}: {message}")
