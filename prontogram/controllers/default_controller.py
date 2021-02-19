import connexion
import six
import pika
from json import dumps

from prontogram.models.error import Error  # noqa: E501
from prontogram.models.message import Message  # noqa: E501
from prontogram import util
from datetime import datetime


def send_message(message=None):  # noqa: E501
    """sendMessage

    Sends the message to ProntoGram for being dispatched to the actual user. API for: ACMESky # noqa: E501

    :param message: 
    :type message: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        message = Message.from_dict(connexion.request.get_json())  # noqa: E501
    connection = pika.BlockingConnection(pika.ConnectionParameters('prontogram_mq'))
    channel = connection.channel()

    """
    Creates a queue with name message.receiver if it does not exist, otherwise does nothing.
    Flag durable set to True requires the queue to be persistent on restart.
    """
    channel.queue_declare(queue=message.receiver, durable=True)

    message.send_time = datetime.now().isoformat()

    channel.basic_publish(exchange='',
                          routing_key=message.receiver,
                          body=bytes(dumps(message.to_dict(), default=str), 'utf-8'),
                          properties=pika.BasicProperties(delivery_mode=2)
                          )

    connection.close()

    return ("", 200)
