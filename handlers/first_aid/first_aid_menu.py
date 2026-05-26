from services.messages.sender import send_message
from services.navigation.navigation import open_menu

from keyboards.first_aid.first_aid_keyboard import (
    get_first_aid_keyboard
)


def handle_first_aid_menu(vk, user_id):
    open_menu(user_id, "first_aid_menu")

    message = (
        "🩺 Первая помощь\n\n"
        "Выберите ситуацию:"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=message,
        keyboard=get_first_aid_keyboard()
    )