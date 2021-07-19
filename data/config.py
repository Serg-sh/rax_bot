from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")  # Список админов
MANAGERS = env.list("MANAGERS")  # Список менеджеров
IP = env.str("IP")  # адрес хоста


