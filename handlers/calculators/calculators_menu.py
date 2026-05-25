from keyboards.calculators.calculators_keyboard import (
    get_calculators_keyboard
)

from services.navigation.navigation import open_menu
from services.messages.sender import send_message


def handle_calculators_menu(vk, user_id):
    open_menu(user_id, "calculators_menu")

    message = (
        "🧮 Калькуляторы\n\n"
        "Выберите нужный расчёт:"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=message,
        keyboard=get_calculators_keyboard()
    )