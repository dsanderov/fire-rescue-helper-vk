from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_gdzs_device_keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        "ДАСВ",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_button(
        "ДАСК",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⬅ Главное меню",
        color=VkKeyboardColor.POSITIVE
    )

    return keyboard.get_keyboard()