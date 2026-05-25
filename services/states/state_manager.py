# =========================================
# ХРАНИЛИЩЕ СОСТОЯНИЙ ПОЛЬЗОВАТЕЛЕЙ
# =========================================

user_states = {}


# =========================================
# УСТАНОВИТЬ СОСТОЯНИЕ
# =========================================

def set_state(user_id, state_name, data=None):

    # Если пользователь уже есть —
    # сохраняем старые data
    old_data = {}

    if user_id in user_states:
        old_data = user_states[user_id]["data"]

    # Если передали новые data —
    # объединяем
    if data is not None:
        old_data.update(data)

    user_states[user_id] = {
        "state": state_name,
        "data": old_data
    }


# =========================================
# ПОЛУЧИТЬ СОСТОЯНИЕ
# =========================================

def get_state(user_id):

    if user_id not in user_states:
        return None

    return user_states[user_id]["state"]


# =========================================
# ПОЛУЧИТЬ DATA
# =========================================

def get_state_data(user_id):

    if user_id not in user_states:
        return {}

    return user_states[user_id]["data"]


# =========================================
# ОБНОВИТЬ DATA
# =========================================

def update_state_data(user_id, new_data):

    if user_id not in user_states:

        user_states[user_id] = {
            "state": None,
            "data": {}
        }

    user_states[user_id]["data"].update(
        new_data
    )


# =========================================
# ОЧИСТИТЬ СОСТОЯНИЕ
# =========================================

def clear_state(user_id):

    if user_id in user_states:
        del user_states[user_id]


# =========================================
# ПРОВЕРКА СОСТОЯНИЯ
# =========================================

def is_state(user_id, state_name):

    return get_state(user_id) == state_name