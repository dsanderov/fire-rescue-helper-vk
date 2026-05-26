from handlers.first_aid.first_aid_menu import (
    handle_first_aid_menu
)

from handlers.first_aid.unconscious_person import (
    handle_unconscious_person
)

from handlers.first_aid.no_breathing_cpr import (
    handle_no_breathing_cpr
)

from handlers.first_aid.bleeding import (
    handle_bleeding
)

from handlers.first_aid.carbon_monoxide import (
    handle_carbon_monoxide
)

from handlers.first_aid.electrical_injury import (
    handle_electrical_injury
)

from services.messages.sender import send_message


def handle_first_aid_router(vk, user_id, text):
    if text == "🩺 первая помощь":
        handle_first_aid_menu(vk, user_id)
        return True

    if text == "🚫 нет сознания":
        handle_unconscious_person(vk, user_id)
        return True

    if text == "🫁 нет дыхания / слр":
        handle_no_breathing_cpr(vk, user_id)
        return True

    if text == "🩸 кровотечение":
        handle_bleeding(vk, user_id)
        return True

    if text == "☠ отравление co":
        handle_carbon_monoxide(vk, user_id)
        return True

    if text == "⚡ электротравма":
        handle_electrical_injury(vk, user_id)
        return True

    first_aid_stub_messages = {
        "🔥 ожоги": "Раздел «Ожоги» пока в разработке.",
        "🧊 обморожения": "Раздел «Обморожения» пока в разработке.",
        "🦴 переломы": "Раздел «Переломы» пока в разработке.",
        "🫀 шок": "Раздел «Шок» пока в разработке.",
        "🫁 инородное тело": "Раздел «Инородное тело дыхательных путей» пока в разработке.",
        "🚑 сортировка": "Раздел «Сортировка пострадавших» пока в разработке."
    }

    if text in first_aid_stub_messages:
        send_message(
            vk=vk,
            user_id=user_id,
            message=first_aid_stub_messages[text]
        )
        return True

    return False