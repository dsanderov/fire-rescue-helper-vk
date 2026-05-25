from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_gdzs_keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        "▶ Начать расчёт ГДЗС",
        color=VkKeyboardColor.POSITIVE
    )

    keyboard.add_line()

    keyboard.add_button(
        "📖 Формулы расчёта",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⬅ Главное меню",
        color=VkKeyboardColor.POSITIVE
    )

    return keyboard.get_keyboard()