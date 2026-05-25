from handlers.menu import handle_main_menu

from handlers.situations.situations_menu import (
    handle_situations_menu
)

from handlers.calculators.calculators_menu import (
    handle_calculators_menu
)


def handle_main_router(vk, user_id, text):

    if text in [
        "start",
        "/start",
        "начать",
        "меню"
    ]:
        handle_main_menu(vk, user_id)
        return True

    if text == "🚒 ситуации":
        handle_situations_menu(vk, user_id)
        return True

    if text == "🧮 калькуляторы":
        handle_calculators_menu(vk, user_id)
        return True

    return False