from keyboards.main_keyboard import get_main_keyboard

from services.navigation.navigation import open_menu
from services.messages.sender import send_message


def handle_main_menu(vk, user_id):
    open_menu(user_id, "main_menu")

    message = (
        "🚒 Помощник пожарного-спасателя\n\n"
        "Выберите раздел:"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=message,
        keyboard=get_main_keyboard()
    )