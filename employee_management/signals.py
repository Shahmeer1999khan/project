from django.db.models.signals import Signal
from django.dispatch import receiver
import redis
import json

redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

signal = Signal()

@receiver(signal)
def signal_handler(sender,**kwargs):
    print('signal received:',sender, kwargs)
    
    
    
    channel_name = 'signal'
    custom_data = json.dumps(kwargs.get('custom_data', {}))
    redis_client.publish(channel_name, custom_data)
    
