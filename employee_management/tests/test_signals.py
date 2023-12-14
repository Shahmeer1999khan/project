from django.test import TestCase
from django.core.cache import cache
from django.db.models.signals import Signal
from django.dispatch import receiver
import redis
import json
import time 
time.sleep(1)

redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

class RedisPubSubTest(TestCase):
    def setUp(self):
        self.redis_test_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)

    def tearDown(self):
        self.redis_test_client.flushdb()

    def test_signal_handler(self):
        signal = Signal()

        @receiver(signal)
        def test_signal_handler(sender, **kwargs):
            self.assertEqual(sender, None)
            self.assertEqual(kwargs['custom_data'], 'Hello!')
            self.signal_handler_called = True

        self.signal_handler_called = False

        signal.send(sender=None, custom_data="Hello!")

        self.assertTrue(self.signal_handler_called)

    def test_redis_pub_sub(self):
        signal = Signal()

        @receiver(signal)
        def test_signal_handler(sender, **kwargs):
            channel_name = 'signal'
            custom_data = json.dumps(kwargs.get('custom_data', {}))
            self.redis_test_client.publish(channel_name, custom_data)

        signal.send(sender=None, custom_data="Hello!")
        print("signal sent")
        time.sleep(1)


        message = self.redis_test_client.blpop('signal', timeout=10)
        print("message received", message)
        self.assertIsNotNone(message)
        
        channel, received_data = message
        received_data = json.loads(received_data)
        self.assertEqual(received_data['custom_data'], 'Hello!')

if __name__ == '__main__':
    import unittest
    unittest.main()
