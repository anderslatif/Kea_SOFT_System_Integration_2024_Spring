import redis
from rq import Queue
from utils import perform_task

redis_client = redis.Redis(host='localhost', port=6379, db=0)

queue = Queue(connection=redis_client)

for _ in range(15):
    queue.enqueue(perform_task)
    