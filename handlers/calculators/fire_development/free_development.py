from services.messages.sender import send_message

from services.states.state_manager import (
    set_state,
    update_state_data,
    get_state_data,
    clear_state
)

from services.calculations.fire_development.free_development import (
    calculate_free_fire_development
)

from keyboards.calculators.fire_development.free_development_keyboard import (
    get_aps_keyboard,
    get_season_keyboard,
    get_winter_deployment_keyboard
)


def handle_free_development_start(vk, user_id):
    clear_state(user_id)

    set_state(
        user_id,
        "free_fire_waiting_aps",
        {}
    )

    message = (
        "🔥 Время свободного развития пожара\n\n"
        "Формула расчёта:\n"
        "Tсв = Tд.с + Tсб + Tсл + Tб.р\n\n"
        "Где:\n"
        "Tд.с — время до сообщения о пожаре;\n"
        "Tсб — время сбора личного состава по тревоге;\n"
        "Tсл — время следования к месту вызова;\n"
        "Tб.р — время боевого развёртывания.\n\n"
        "Выберите наличие АПС на объекте.\n\n"
        "Если наличие АПС неизвестно, расчёт выполняется как при её отсутствии."
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=message,
        keyboard=get_aps_keyboard()
    )


def handle_aps_input(vk, user_id, text):
    if text == "✅ апс есть":
        aps_present = True

    elif text == "❓ апс неизвестно / отсутствует":
        aps_present = False

    else:
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Выберите наличие АПС кнопкой.",
            keyboard=get_aps_keyboard()
        )
        return True

    update_state_data(
        user_id,
        {
            "aps_present": aps_present
        }
    )

    set_state(
        user_id,
        "free_fire_waiting_travel_time"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=(
            "Введите время следования к месту вызова Tсл в минутах.\n\n"
            "Пример: 7"
        )
    )

    return True


def handle_travel_time_input(vk, user_id, text):
    try:
        travel_time = float(text.replace(",", "."))
    except ValueError:
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Введите время следования числом. Например: 7"
        )
        return True

    if travel_time < 0:
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Время следования не может быть отрицательным."
        )
        return True

    update_state_data(
        user_id,
        {
            "travel_time": travel_time
        }
    )

    set_state(
        user_id,
        "free_fire_waiting_deployment"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=(
            "Выберите время боевого развёртывания Tб.р.\n\n"
            "По принятой логике:\n"
            "• летний период — 3 минуты;\n"
            "• зимний период — 6–8 минут;\n"
            "• также можно ввести значение вручную."
        ),
        keyboard=get_season_keyboard()
    )

    return True


def handle_deployment_input(vk, user_id, text):
    if text == "☀ летний период":
        deployment_time = 3
        return finish_free_development_calculation(
            vk,
            user_id,
            deployment_time
        )

    if text == "❄ зимний период":
        set_state(
            user_id,
            "free_fire_waiting_winter_deployment"
        )

        send_message(
            vk=vk,
            user_id=user_id,
            message=(
                "Выберите время боевого развёртывания "
                "для зимнего периода Tб.р:"
            ),
            keyboard=get_winter_deployment_keyboard()
        )

        return True

    if text == "✏ ввести вручную":
        set_state(
            user_id,
            "free_fire_waiting_manual_deployment"
        )

        send_message(
            vk=vk,
            user_id=user_id,
            message=(
                "Введите время боевого развёртывания Tб.р в минутах.\n\n"
                "Пример: 5"
            )
        )

        return True

    send_message(
        vk=vk,
        user_id=user_id,
        message="❌ Выберите вариант кнопкой.",
        keyboard=get_season_keyboard()
    )

    return True


def handle_winter_deployment_input(vk, user_id, text):
    if text not in ["6", "7", "8"]:
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Для зимнего периода выберите 6, 7 или 8 минут.",
            keyboard=get_winter_deployment_keyboard()
        )
        return True

    deployment_time = float(text)

    return finish_free_development_calculation(
        vk,
        user_id,
        deployment_time
    )


def handle_manual_deployment_input(vk, user_id, text):
    try:
        deployment_time = float(text.replace(",", "."))
    except ValueError:
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Введите время боевого развёртывания числом. Например: 5"
        )
        return True

    if deployment_time < 0:
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Время боевого развёртывания не может быть отрицательным."
        )
        return True

    return finish_free_development_calculation(
        vk,
        user_id,
        deployment_time
    )


def finish_free_development_calculation(
    vk,
    user_id,
    deployment_time
):
    data = get_state_data(user_id)

    result = calculate_free_fire_development(
        aps_present=data["aps_present"],
        travel_time=data["travel_time"],
        deployment_time=deployment_time
    )

    clear_state(user_id)

    send_message(
        vk=vk,
        user_id=user_id,
        message=format_free_development_result(result)
    )

    return True


def format_free_development_result(result):
    aps_text = (
        "АПС имеется"
        if result["aps_present"]
        else "АПС отсутствует или наличие неизвестно"
    )

    return (
        "🔥 Расчёт времени свободного развития пожара\n\n"
        "Время свободного развития пожара — это промежуток времени "
        "от момента возникновения горения до момента подачи первых "
        "огнетушащих веществ на его тушение.\n\n"

        "Формула:\n"
        "Tсв = Tд.с + Tсб + Tсл + Tб.р\n\n"

        "Исходные данные:\n"
        f"• {aps_text}\n"
        f"• Tд.с = {format_number(result['detection_message_time'])} мин\n"
        f"• Tсб = {format_number(result['alarm_assembly_time'])} мин\n"
        f"• Tсл = {format_number(result['travel_time'])} мин\n"
        f"• Tб.р = {format_number(result['deployment_time'])} мин\n\n"

        "Расчёт:\n"
        f"Tсв = {format_number(result['detection_message_time'])} "
        f"+ {format_number(result['alarm_assembly_time'])} "
        f"+ {format_number(result['travel_time'])} "
        f"+ {format_number(result['deployment_time'])} "
        f"= {format_number(result['total_time'])} мин\n\n"

        f"📌 Время свободного развития пожара: "
        f"{format_number(result['total_time'])} мин"
    )


def format_number(value):
    if float(value).is_integer():
        return str(int(value))

    return f"{value:.1f}"