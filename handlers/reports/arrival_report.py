from services.messages.sender import send_message

from services.states.state_manager import (
    set_state,
    get_state,
    update_state_data,
    get_state_data,
    clear_state
)

from services.generators.reports.arrival_report_generator import (
    generate_arrival_report
)

from keyboards.reports.skip_characteristics_keyboard import (
    get_skip_characteristics_keyboard
)


def handle_arrival_report_start(vk, user_id):
    clear_state(user_id)

    set_state(
        user_id,
        "arrival_report_address"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=(
            "🚒 Доклад по прибытии\n\n"
            "Введите адрес вызова."
        )
    )


def handle_arrival_report_router(vk, user_id, text):
    state = get_state(user_id)

    if state == "arrival_report_address":
        update_state_data(
            user_id,
            {"address": text}
        )

        set_state(
            user_id,
            "arrival_report_object"
        )

        send_message(
            vk=vk,
            user_id=user_id,
            message="Введите тип объекта.",
        )

        return True

    if state == "arrival_report_object":
        update_state_data(
            user_id,
            {"object_type": text}
        )

        set_state(
            user_id,
            "arrival_report_characteristics"
        )

        send_message(
            vk=vk,
            user_id=user_id,
            message=(
                "Введите характеристику объекта.\n\n"
                "Например:\n"
                "9-этажный панельный многоподъездный жилой дом"
            ),
            keyboard=get_skip_characteristics_keyboard()
        )

        return True

    if state == "arrival_report_characteristics":

        if text == "❌ без уточнения характеристик":
            characteristics = None
        else:
            characteristics = text

        update_state_data(
            user_id,
            {"characteristics": characteristics}
        )

        set_state(
            user_id,
            "arrival_report_signs"
        )

        send_message(
            vk=vk,
            user_id=user_id,
            message="Введите внешние признаки пожара."
        )

        return True

    if state == "arrival_report_signs":
        update_state_data(
            user_id,
            {"fire_signs": text}
        )

        set_state(
            user_id,
            "arrival_report_burning"
        )

        send_message(
            vk=vk,
            user_id=user_id,
            message="Что горит?"
        )

        return True

    if state == "arrival_report_burning":
        update_state_data(
            user_id,
            {"burning": text}
        )

        set_state(
            user_id,
            "arrival_report_place"
        )

        send_message(
            vk=vk,
            user_id=user_id,
            message="Введите место пожара."
        )

        return True

    if state == "arrival_report_place":
        update_state_data(
            user_id,
            {"fire_place": text}
        )

        set_state(
            user_id,
            "arrival_report_people"
        )

        send_message(
            vk=vk,
            user_id=user_id,
            message="Есть ли угроза людям?"
        )

        return True

    if state == "arrival_report_people":
        update_state_data(
            user_id,
            {"people_threat": text}
        )

        set_state(
            user_id,
            "arrival_report_forces"
        )

        send_message(
            vk=vk,
            user_id=user_id,
            message="Какие силы и средства на месте?"
        )

        return True

    if state == "arrival_report_forces":
        update_state_data(
            user_id,
            {"forces": text}
        )

        set_state(
            user_id,
            "arrival_report_actions"
        )

        send_message(
            vk=vk,
            user_id=user_id,
            message="Какие действия проводятся?"
        )

        return True

    if state == "arrival_report_actions":
        update_state_data(
            user_id,
            {"actions": text}
        )

        set_state(
            user_id,
            "arrival_report_additional"
        )

        send_message(
            vk=vk,
            user_id=user_id,
            message="Что требуется дополнительно?"
        )

        return True

    if state == "arrival_report_additional":
        update_state_data(
            user_id,
            {"additional": text}
        )

        data = get_state_data(user_id)

        report = generate_arrival_report(data)

        clear_state(user_id)

        send_message(
            vk=vk,
            user_id=user_id,
            message=report
        )

        return True

    return False