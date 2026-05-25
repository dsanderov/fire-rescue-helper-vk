user_navigation = {}


def open_menu(user_id, menu_name):
    if user_id not in user_navigation:
        user_navigation[user_id] = {
            "current_menu": None,
            "history": []
        }

    current_menu = user_navigation[user_id]["current_menu"]

    if current_menu is not None and current_menu != menu_name:
        user_navigation[user_id]["history"].append(current_menu)

    user_navigation[user_id]["current_menu"] = menu_name


def get_current_menu(user_id):
    if user_id not in user_navigation:
        return None

    return user_navigation[user_id]["current_menu"]


def go_back(user_id):
    if user_id not in user_navigation:
        return None

    history = user_navigation[user_id]["history"]

    if not history:
        return None

    previous_menu = history.pop()
    user_navigation[user_id]["current_menu"] = previous_menu

    return previous_menu


def clear_history(user_id):
    if user_id not in user_navigation:
        return

    user_navigation[user_id]["history"] = []


def reset_navigation(user_id):
    user_navigation[user_id] = {
        "current_menu": None,
        "history": []
    }