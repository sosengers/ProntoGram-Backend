# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from prontogram.models.error import Error  # noqa: E501
from prontogram.models.message import Message  # noqa: E501
from prontogram.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_send_message(self):
        """Test case for send_message

        sendMessage
        """
        message = {
  "receiver" : "receiver",
  "sender" : "sender",
  "body" : "body"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/messages',
            method='POST',
            headers=headers,
            data=json.dumps(message),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
