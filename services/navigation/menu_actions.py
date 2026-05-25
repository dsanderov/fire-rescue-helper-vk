from services.navigation.menu_registry import get_menu_handler


def open_registered_menu(vk, user_id, menu_name):
    handler = get_menu_handler(menu_name)

    if handler is None:
        return False

    handler(vk, user_id)
    return True