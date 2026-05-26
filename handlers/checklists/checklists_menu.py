from services.messages.sender import send_message
from services.navigation.navigation import open_menu

from keyboards.checklists.checklists_keyboard import (
    get_checklists_keyboard
)


def handle_checklists_menu(vk, user_id):
    open_menu(user_id, "checklists_menu")

    message = (
        "📋 Чек-листы\n\n"
        "Выберите чек-лист:"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=message,
        keyboard=get_checklists_keyboard()
    )