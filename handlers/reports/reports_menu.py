from services.messages.sender import send_message

from keyboards.reports.reports_keyboard import (
    get_reports_keyboard
)


def handle_reports_menu(vk, user_id):
    message = (
        "📡 Радиодоклады\n\n"
        "Выберите тип доклада."
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=message,
        keyboard=get_reports_keyboard()
    )