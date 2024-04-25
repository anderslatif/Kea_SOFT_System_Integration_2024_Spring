import redis
from rq import Queue, Worker

redis_client = redis.Redis(host='localhost', port=6379, db=0)

queue = Queue(connection=redis_client)

worker = Worker(queues=[queue], connection=redis_client)
worker.work(with_scheduler=True)
