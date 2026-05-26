from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor


def get_skip_characteristics_keyboard():
    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button(
        "❌ Без уточнения характеристик",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    keyboard.add_button(
        "❌ Отмена",
        color=VkKeyboardColor.NEGATIVE
    )

    return keyboard.get_keyboard()