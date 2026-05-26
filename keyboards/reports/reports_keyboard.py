from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor


def get_reports_keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(
        "🚒 Доклад по прибытии",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "⬅ Главное меню",
        color=VkKeyboardColor.POSITIVE
    )

    return keyboard.get_keyboard()