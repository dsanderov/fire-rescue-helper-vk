from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_fires_keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        "🏢 Пожар в квартире",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⬇ Пожар в подвале",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_button(
        "⬆ Пожар на чердаке",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "🏠 Частный дом",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_button(
        "🏬 ТЦ",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⬅ Главное меню",
        color=VkKeyboardColor.POSITIVE
    )

    return keyboard.get_keyboard()


def get_apartment_fire_keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        "🚨 Опасности квартиры",
        color=VkKeyboardColor.NEGATIVE
    )

    keyboard.add_button(
        "🔍 Разведка квартиры",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "🧯 Решающее направление",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_button(
        "🚒 Первые действия",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "🫁 ГДЗС квартира",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_button(
        "📡 Доклад квартира",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "❌ Ошибки квартира",
        color=VkKeyboardColor.NEGATIVE
    )

    keyboard.add_button(
        "📌 Важно квартира",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⬅ Главное меню",
        color=VkKeyboardColor.POSITIVE
    )

    return keyboard.get_keyboard()