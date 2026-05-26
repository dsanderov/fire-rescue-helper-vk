user_states = {}
user_state_data = {}


def set_state(user_id, state, data=None):
    user_states[user_id] = state

    if data is not None:
        user_state_data[user_id] = data


def get_state(user_id):
    return user_states.get(user_id)


def update_state_data(user_id, data):
    if user_id not in user_state_data:
        user_state_data[user_id] = {}

    user_state_data[user_id].update(data)


def get_state_data(user_id):
    return user_state_data.get(user_id, {})


def clear_state(user_id):
    if user_id in user_states:
        del user_states[user_id]

    if user_id in user_state_data:
        del user_state_data[user_id]