from exceptions import LoadEnvException
import dotenv
import os

dotenv.load_dotenv('.env')

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise LoadEnvException()

try:
    TIME_LIMIT = float(os.getenv('TIME_LIMIT'))
except ValueError:
    raise LoadEnvException()
