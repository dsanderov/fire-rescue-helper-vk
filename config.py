import os

from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv("VK_TOKEN")


if not TOKEN:
    raise RuntimeError(
        "Не найден VK_TOKEN. Проверь файл .env"
    )