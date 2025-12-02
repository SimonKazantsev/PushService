import pika
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RabbitMQConsumer:
    def __init__(self, rabbitmq_url, queue_name):
        self.rabbitmq_url = rabbitmq_url
        self.queue_name = queue_name
        self.connection = None
        self.channel = None


    def connect(self):
        """Устанавливает соединение с RabbitMQ."""
        self.connection = pika.BlockingConnection(pika.URLParameters(self.rabbitmq_url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=True)

    def callback(self, ch, method, properties, body):
        """Обрабатывает полученные сообщения."""
        message = json.loads(body)
        logger.info(f"Received message: {message}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        """Запускает процесс прослушивания очереди."""
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback)
        logger.info("Consuming...")
        
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            logger.info("Stopping consumer...")
            self.channel.stop_consuming()
        finally:
            self.close_connection()

    def close_connection(self):
        """Закрывает соединение с RabbitMQ."""
        if self.connection:
            self.connection.close()