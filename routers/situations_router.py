from handlers.situations.situations_menu import (
    handle_situations_menu
)

from handlers.situations.fires.fires_menu import (
    handle_fires_menu
)

from handlers.situations.fires.apartment_fire import (
    handle_apartment_fire_menu,
    handle_apartment_fire_dangers,
    handle_apartment_fire_recon,
    handle_apartment_fire_direction,
    handle_apartment_fire_first_actions,
    handle_apartment_fire_gdzs,
    handle_apartment_fire_report,
    handle_apartment_fire_mistakes,
    handle_apartment_fire_important
)

from services.messages.sender import send_message


def handle_situations_router(vk, user_id, text):

    if text == "🚒 ситуации":
        handle_situations_menu(vk, user_id)
        return True

    if text == "🔥 пожары":
        handle_fires_menu(vk, user_id)
        return True

    if text == "🏢 пожар в квартире":
        handle_apartment_fire_menu(vk, user_id)
        return True

    if text == "🚨 опасности квартиры":
        handle_apartment_fire_dangers(vk, user_id)
        return True

    if text == "🔍 разведка квартиры":
        handle_apartment_fire_recon(vk, user_id)
        return True

    if text == "🧯 решающее направление":
        handle_apartment_fire_direction(vk, user_id)
        return True

    if text == "🚒 первые действия":
        handle_apartment_fire_first_actions(vk, user_id)
        return True

    if text == "🫁 гдзс квартира":
        handle_apartment_fire_gdzs(vk, user_id)
        return True

    if text == "📡 доклад квартира":
        handle_apartment_fire_report(vk, user_id)
        return True

    if text == "❌ ошибки квартира":
        handle_apartment_fire_mistakes(vk, user_id)
        return True

    if text == "📌 важно квартира":
        handle_apartment_fire_important(vk, user_id)
        return True

    situation_stub_messages = {
        "🚗 дтп": "Раздел ДТП пока в разработке.",
        "☣ химия и газ": "Раздел химии и газа пока в разработке.",
        "⚡ электрика": "Раздел электрики пока в разработке.",
        "🌊 вода и лёд": "Раздел воды и льда пока в разработке.",
        "🏗 завалы": "Раздел завалов пока в разработке.",
        "⬇ пожар в подвале": "Карточка «Пожар в подвале» пока в разработке.",
        "⬆ пожар на чердаке": "Карточка «Пожар на чердаке» пока в разработке.",
        "🏠 частный дом": "Карточка «Частный дом» пока в разработке.",
        "🏬 тц": "Карточка «ТЦ» пока в разработке."
    }

    if text in situation_stub_messages:
        send_message(
            vk=vk,
            user_id=user_id,
            message=situation_stub_messages[text]
        )
        return True

    return False