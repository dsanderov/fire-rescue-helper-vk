from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_first_aid_keyboard():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button("🚫 Нет сознания", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("🫁 Нет дыхания / СЛР", color=VkKeyboardColor.PRIMARY)

    keyboard.add_line()

    keyboard.add_button("🩸 Кровотечение", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("🔥 Ожоги", color=VkKeyboardColor.PRIMARY)

    keyboard.add_line()

    keyboard.add_button("🧊 Обморожения", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("☠ Отравление CO", color=VkKeyboardColor.PRIMARY)

    keyboard.add_line()

    keyboard.add_button("⚡ Электротравма", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("🦴 Переломы", color=VkKeyboardColor.PRIMARY)

    keyboard.add_line()

    keyboard.add_button("🫀 Шок", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("🫁 Инородное тело", color=VkKeyboardColor.PRIMARY)

    keyboard.add_line()

    keyboard.add_button("🚑 Сортировка", color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()

    keyboard.add_button("⬅ Главное меню", color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()