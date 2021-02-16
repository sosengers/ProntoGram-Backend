import connexion
import six

from prontogram.models.error import Error  # noqa: E501
from prontogram.models.message import Message  # noqa: E501
from prontogram import util


def send_message(message=None):  # noqa: E501
    """sendMessage

    Sends the message to ProntoGram for being dispatched to the actual user. API for: ACMESky # noqa: E501

    :param message: 
    :type message: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        message = Message.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
