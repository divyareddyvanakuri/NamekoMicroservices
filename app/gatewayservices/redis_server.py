from redis import StrictRedis
import redis

class Redis:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0):
        self.host = redis_host
        self.port = redis_port
        self.db = redis_db
        self.con = self.connect()

    def connect(self):
        try:
            con = self.con = redis.StrictRedis(
            host=self.host,
            port=self.port,
            db=self.db)
            if con:
                print('Redis is connected : ', con)
                return con
        except Exception as e:
            print(e)
            print("RedisUtil Connection Error")
            con = self.con = None

    def get(self, redis_key):
        # print(redis_key)
        return self.con.get(redis_key)