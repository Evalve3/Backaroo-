from envparse import env

env.read_envfile('.env')

username = env.str('DATABASE_USERNAME')
password = env.str('DATABASE_PASSWORD')
port = env.int('DATABASE_PORT')
hostname = env.str('DATABASE_HOSTNAME')
dbname = env.str('DATABASE_NAME')

REAL_DATABASE_URL = f"postgresql+asyncpg://{username}:{password}@{hostname}:{port}/{dbname}"
ACCESS_TOKEN_EXPIRE_MINUTES = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=3600)
SECRET_KEY: str = env.str("SECRET_KEY", default="secret_key")
JWT_ALGORITHM: str = env.str("JWT_ALGORITHM", default="HS256")
