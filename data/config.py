from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")  # Список админов
MANAGERS = env.list("MANAGERS")  # Список менеджеров
db_host = env.str("HOST_DB")  # адрес хоста базы данных
db_name = env.str("NAME_DB") # Имя БД
db_user = env.str("USER_DB") # юзер бд
db_pass = env.str("PASS_DB") # пароль БД

