# =========================================
# УНИВЕРСАЛЬНАЯ ОТПРАВКА СООБЩЕНИЙ
# =========================================

def send_message(
    vk,
    user_id,
    message,
    keyboard=None
):

    try:

        vk.messages.send(
            user_id=user_id,
            message=message,
            keyboard=keyboard,
            random_id=0
        )

    except Exception as error:

        print(
            f"[ОШИБКА ОТПРАВКИ СООБЩЕНИЯ] {error}"
        )