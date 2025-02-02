import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)


def get_key(key):
    return redis_client.get(key)


def set_key(key, value):
    return redis_client.set(key, value)


def has_key(key):
    return redis_client.exists(key)