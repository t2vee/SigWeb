from redis import asyncio as aioredis

from Utils.Config import settings


class RedisConnection:
    def __init__(self):
        self.db = None

    def __call__(self, *args, **kwargs):
        await db.set_bind(f'postgresql://'
                          f'{settings.POSTGRES_USER}:'
                          f'{settings.POSTGRES_PASSWORD}@'
                          f'{settings.POSTGRES_HOST}/'
                          f'{settings.POSTGRES_NAME}')

        pool = aioredis.ConnectionPool.from_url(f'redis://{settings.REDIS_ADDRESS}:{settings.REDIS_PORT}')
        self.db = aioredis.Redis(connection_pool=pool)
