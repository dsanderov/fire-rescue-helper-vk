from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_aps_keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        "✅ АПС есть",
        color=VkKeyboardColor.POSITIVE
    )

    keyboard.add_line()

    keyboard.add_button(
        "❓ АПС неизвестно / отсутствует",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⬅ Главное меню",
        color=VkKeyboardColor.POSITIVE
    )

    return keyboard.get_keyboard()


def get_season_keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        "☀ Летний период",
        color=VkKeyboardColor.POSITIVE
    )

    keyboard.add_line()

    keyboard.add_button(
        "❄ Зимний период",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "✏ Ввести вручную",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⬅ Главное меню",
        color=VkKeyboardColor.POSITIVE
    )

    return keyboard.get_keyboard()


def get_winter_deployment_keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        "6",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_button(
        "7",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_button(
        "8",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⬅ Главное меню",
        color=VkKeyboardColor.POSITIVE
    )

    return keyboard.get_keyboard()