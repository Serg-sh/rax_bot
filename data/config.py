from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")  # Список админов
IP = env.str("IP")  # адрес хоста

managers_id = [
    '1806701232',
]
