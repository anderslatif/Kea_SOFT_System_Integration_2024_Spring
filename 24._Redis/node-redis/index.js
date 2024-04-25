import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('connect', () => console.log('Connected to Redis'));
redisClient.on('error', (error) => console.error('Error:', error));

await redisClient.connect();


// redisClient.set("myKey", "some value");
const value = await redisClient.get("myKey");
console.log(value);

// redisClient.setEx("myKey", 10, "some value");
