from keyboards.situations.situations_keyboard import (
    get_situations_keyboard
)

from services.navigation.navigation import open_menu
from services.messages.sender import send_message


def handle_situations_menu(vk, user_id):
    open_menu(user_id, "situations_menu")

    message = (
        "🚒 Раздел ситуаций\n\n"
        "Выберите тип происшествия:"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=message,
        keyboard=get_situations_keyboard()
    )