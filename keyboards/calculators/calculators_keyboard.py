from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_calculators_keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        "🫁 Воздух ГДЗС",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "💧 Вода в АЦ",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_button(
        "🚿 Рукавные линии",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "🧯 Пенообразователь",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⬅ Главное меню",
        color=VkKeyboardColor.POSITIVE
    )

    return keyboard.get_keyboard()