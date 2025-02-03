import redis
from core import settings

redis_client = redis.Redis(host=settings.REDIS_HOST, db=settings.REDIS_DB, port=settings.REDIS_PORT)


def get_key(key):
    return redis_client.get(key)


def set_key(key, value):
    return redis_client.set(key, value)


def has_key(key):
    return redis_client.exists(key)