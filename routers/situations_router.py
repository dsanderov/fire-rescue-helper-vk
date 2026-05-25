from services.messages.sender import send_message


def handle_situations_router(vk, user_id, text):
    if text == "🔥 пожары":
        send_message(
            vk=vk,
            user_id=user_id,
            message="Раздел пожаров пока в разработке."
        )
        return True

    if text == "🚗 дтп":
        send_message(
            vk=vk,
            user_id=user_id,
            message="Раздел ДТП пока в разработке."
        )
        return True

    if text == "☣ химия и газ":
        send_message(
            vk=vk,
            user_id=user_id,
            message="Раздел химии и газа пока в разработке."
        )
        return True

    if text == "⚡ электрика":
        send_message(
            vk=vk,
            user_id=user_id,
            message="Раздел электрики пока в разработке."
        )
        return True

    if text == "🌊 вода и лёд":
        send_message(
            vk=vk,
            user_id=user_id,
            message="Раздел воды и льда пока в разработке."
        )
        return True

    if text == "🏗 завалы":
        send_message(
            vk=vk,
            user_id=user_id,
            message="Раздел завалов пока в разработке."
        )
        return True

    return False