import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

pubsub = redis_client.pubsub()

pubsub.subscribe('myChannel')

for message in pubsub.listen():
    print(message)

    if message['data'] == b'quit':
        break
