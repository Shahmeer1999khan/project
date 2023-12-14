import redis

redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
channel_name = 'signal'

pubsub = redis_client.pubsub()
pubsub.subscribe(channel_name)

for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Received message: {message['data'].decode('utf-8')}")
