# Running Redis in Docker

First pull the Redis image:

```bash 
$ docker pull redis
```
Create and start the network:

```bash 
$ docker network create redis-net
$ docker run --network redis-net --name my-redis -d redis
```
---

# Run the CLI:

From now on just run this to run the CLI:

```bash
$ docker run -it --network redis-net --rm redis redis-cli -h my-redis
```

---

# Redis Benchmarks

To run the Redis benchmark tool:

```bash
$ docker run -it --network redis-net --rm redis redis-benchmark -h my-redis -p 6379
```