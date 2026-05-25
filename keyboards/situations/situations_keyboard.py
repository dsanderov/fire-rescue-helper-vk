from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor


def get_situations_keyboard():

    keyboard = VkKeyboard(one_time=False)

    # =========================================
    # ПОЖАРЫ / ДТП
    # =========================================

    keyboard.add_button(
        "🔥 Пожары",
        color=VkKeyboardColor.NEGATIVE
    )

    keyboard.add_button(
        "🚗 ДТП",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    # =========================================
    # ХИМИЯ / ЭЛЕКТРИКА
    # =========================================

    keyboard.add_button(
        "☣ Химия и газ",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_button(
        "⚡ Электрика",
        color=VkKeyboardColor.SECONDARY
    )

    keyboard.add_line()

    # =========================================
    # ВОДА / ЗАВАЛЫ
    # =========================================

    keyboard.add_button(
        "🌊 Вода и лёд",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_button(
        "🏗 Завалы",
        color=VkKeyboardColor.PRIMARY
    )

    keyboard.add_line()

    # =========================================
    # НАЗАД
    # =========================================

    keyboard.add_button(
        "⬅ Главное меню",
        color=VkKeyboardColor.POSITIVE
    )

    return keyboard.get_keyboard()