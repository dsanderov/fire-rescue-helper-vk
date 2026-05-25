from keyboards.calculators.gdzs.gdzs_device_keyboard import (
    get_gdzs_device_keyboard
)

from services.messages.sender import send_message
from services.states.state_manager import set_state


def handle_gdzs_start(vk, user_id):
    set_state(
        user_id,
        "gdzs_waiting_device",
        {}
    )

    message = (
        "🫁 Расчёт параметров работы в СИЗОД\n\n"
        "Выберите тип СИЗОД:"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=message,
        keyboard=get_gdzs_device_keyboard()
    )