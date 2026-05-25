from keyboards.calculators.gdzs.gdzs_keyboard import (
    get_gdzs_keyboard
)

from services.navigation.navigation import open_menu
from services.messages.sender import send_message


def handle_gdzs_menu(vk, user_id):
    open_menu(user_id, "gdzs_menu")

    message = (
        "🫁 Калькулятор воздуха ГДЗС\n\n"
        "Расчёт будет выполняться по формулам расчёта "
        "параметров работы в СИЗОД.\n\n"
        "Выберите действие:"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=message,
        keyboard=get_gdzs_keyboard()
    )