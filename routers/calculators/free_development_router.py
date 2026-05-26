from services.states.state_manager import get_state

from handlers.calculators.fire_development.free_development import (
    handle_free_development_start,
    handle_aps_input,
    handle_travel_time_input,
    handle_deployment_input,
    handle_winter_deployment_input,
    handle_manual_deployment_input
)


def handle_free_development_router(vk, user_id, text):
    current_state = get_state(user_id)

    if text == "🔥 свободное развитие пожара":
        handle_free_development_start(vk, user_id)
        return True

    if current_state == "free_fire_waiting_aps":
        return handle_aps_input(vk, user_id, text)

    if current_state == "free_fire_waiting_travel_time":
        return handle_travel_time_input(vk, user_id, text)

    if current_state == "free_fire_waiting_deployment":
        return handle_deployment_input(vk, user_id, text)

    if current_state == "free_fire_waiting_winter_deployment":
        return handle_winter_deployment_input(vk, user_id, text)

    if current_state == "free_fire_waiting_manual_deployment":
        return handle_manual_deployment_input(vk, user_id, text)

    return False