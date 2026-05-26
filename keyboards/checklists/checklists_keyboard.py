from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_checklists_keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        "🔍 Разведка пожара",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⬅ Главное меню",
        color=VkKeyboardColor.POSITIVE
    )

    return keyboard.get_keyboard()