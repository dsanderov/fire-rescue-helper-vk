from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_main_keyboard():
    keyboard = VkKeyboard(one_time=False)

    # Первая строка
    keyboard.add_button("🚒 Ситуации", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("🧮 Калькуляторы", color=VkKeyboardColor.PRIMARY)

    keyboard.add_line()

    # Вторая строка
    keyboard.add_button("📋 Чек-листы", color=VkKeyboardColor.SECONDARY)
    keyboard.add_button("📡 Доклады", color=VkKeyboardColor.SECONDARY)

    keyboard.add_line()

    # Третья строка
    keyboard.add_button("☣ Опасности", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button("🩺 Первая помощь", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()

    # Четвертая строка
    keyboard.add_button("🎓 Учебный режим", color=VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()