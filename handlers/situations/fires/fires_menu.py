from services.messages.sender import send_message
from services.navigation.navigation import open_menu

from keyboards.situations.fires.fires_keyboard import (
    get_fires_keyboard
)


def handle_fires_menu(vk, user_id):
    open_menu(user_id, "fires_menu")

    message = (
        "🔥 Пожары\n\n"
        "Выберите тип пожара:"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=message,
        keyboard=get_fires_keyboard()
    )