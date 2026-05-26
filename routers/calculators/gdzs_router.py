from handlers.calculators.gdzs.gdzs_menu import handle_gdzs_menu
from handlers.calculators.gdzs.gdzs_start import handle_gdzs_start

from services.messages.sender import send_message

from services.states.state_manager import (
    get_state,
    get_state_data,
    update_state_data,
    set_state,
    clear_state
)

from services.calculations.gdzs.air_calculator import (
    calculate_gdzs_air
)


def handle_gdzs_router(vk, user_id, text):
    current_state = get_state(user_id)

    if text == "🫁 воздух гдзс":
        handle_gdzs_menu(vk, user_id)
        return True

    if text == "▶ начать расчёт гдзс":
        handle_gdzs_start(vk, user_id)
        return True

    if text == "📖 формулы расчёта":
        send_formulas(vk, user_id)
        return True

    if current_state == "gdzs_waiting_device":
        return handle_device_input(vk, user_id, text)

    if current_state == "gdzs_waiting_pressure":
        return handle_pressure_input(vk, user_id, text)

    if current_state == "gdzs_waiting_volume":
        return handle_volume_input(vk, user_id, text)

    if current_state == "gdzs_waiting_start_time":
        return handle_start_time_input(vk, user_id, text)

    return False


def handle_device_input(vk, user_id, text):
    if text not in ["дасв", "даск"]:
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Выберите ДАСВ или ДАСК кнопкой."
        )
        return True

    device_type = text.upper()

    update_state_data(
        user_id,
        {
            "device_type": device_type
        }
    )

    set_state(user_id, "gdzs_waiting_pressure")

    send_message(
        vk=vk,
        user_id=user_id,
        message=(
            f"Выбран тип СИЗОД: {device_type}\n\n"
            "Введите минимальное давление при включении "
            "Pmin.вкл, кгс/см².\n\n"
            "Пример: 270"
        )
    )

    return True


def handle_pressure_input(vk, user_id, text):
    try:
        p_min = float(text.replace(",", "."))
    except ValueError:
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Введите давление числом. Например: 270"
        )
        return True

    if p_min <= 0:
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Давление должно быть больше нуля."
        )
        return True

    update_state_data(
        user_id,
        {
            "p_min": p_min
        }
    )

    set_state(user_id, "gdzs_waiting_volume")

    send_message(
        vk=vk,
        user_id=user_id,
        message=(
            "Введите общую вместимость баллона/баллонов Vб, л.\n\n"
            "Примеры:\n"
            "6.8\n"
            "7\n"
            "9\n"
            "13.6 для 2×6.8"
        )
    )

    return True


def handle_volume_input(vk, user_id, text):
    try:
        cylinder_volume = float(text.replace(",", "."))
    except ValueError:
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Введите объём числом. Например: 6.8"
        )
        return True

    if cylinder_volume <= 0:
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Объём должен быть больше нуля."
        )
        return True

    update_state_data(
        user_id,
        {
            "cylinder_volume": cylinder_volume
        }
    )

    set_state(user_id, "gdzs_waiting_start_time")

    send_message(
        vk=vk,
        user_id=user_id,
        message=(
            "Введите время включения в СИЗОД Tвкл.\n\n"
            "Формат: ЧЧ:ММ\n"
            "Пример: 14:30"
        )
    )

    return True


def handle_start_time_input(vk, user_id, text):
    if not is_valid_time(text):
        send_message(
            vk=vk,
            user_id=user_id,
            message="❌ Введите время в формате ЧЧ:ММ. Например: 14:30"
        )
        return True

    data = get_state_data(user_id)

    result = calculate_gdzs_air(
        device_type=data["device_type"],
        p_min=data["p_min"],
        cylinder_volume=data["cylinder_volume"],
        start_time=text
    )

    clear_state(user_id)

    send_message(
        vk=vk,
        user_id=user_id,
        message=format_result(result)
    )

    return True


def is_valid_time(text):
    parts = text.split(":")

    if len(parts) != 2:
        return False

    try:
        hours = int(parts[0])
        minutes = int(parts[1])
    except ValueError:
        return False

    return 0 <= hours <= 23 and 0 <= minutes <= 59


def format_number(value):
    if float(value).is_integer():
        return str(int(value))

    return f"{value:.1f}"


def format_result(result):
    device_type = result["device_type"]
    p_min = result["p_min"]
    cylinder_volume = result["cylinder_volume"]
    p_max_drop = result["p_max_drop"]
    p_exit = result["p_exit"]
    delta_time = result["delta_time"]
    total_time = result["total_time"]
    divisor = result["divisor"]

    return (
        "🫁 Расчёт работы звена ГДЗС в СИЗОД\n\n"
        f"Тип аппарата: {device_type}\n"
        f"Pmin.вкл: {format_number(p_min)} кгс/см²\n"
        f"Vб: {format_number(cylinder_volume)} л\n"
        f"Tвкл: {result['start_time']}\n\n"

        "1. Максимально допустимое падение давления:\n"
        f"Pmax.пад = Pmin.вкл / 3 = "
        f"{format_number(p_min)} / 3 = "
        f"{p_max_drop:.1f} кгс/см²\n\n"

        "2. Контрольное давление выхода:\n"
        f"Pк.вых = Pmin.вкл - Pmax.пад = "
        f"{format_number(p_min)} - {p_max_drop:.1f} = "
        f"{p_exit:.1f} кгс/см²\n\n"

        "3. Промежуток времени до подачи команды на возвращение:\n"
        f"ΔT = Pmax.пад × Vб / {divisor} = "
        f"{format_number(p_max_drop)} × "
        f"{format_number(cylinder_volume)} / {divisor} = "
        f"{delta_time:.1f} мин\n\n"

        "4. Время подачи команды на возвращение:\n"
        f"Tвых = Tвкл + ΔT = {result['exit_command_time']}\n\n"

        "5. Общее примерное время работы звена в НДС:\n"
        f"Tобщ = Pmin.вкл × Vб / {divisor} = "
        f"{format_number(p_min)} × "
        f"{format_number(cylinder_volume)} / {divisor} = "
        f"{total_time:.1f} мин\n\n"

        "6. Время обязательного возвращения из НДС:\n"
        f"Tвозвр = Tвкл + Tобщ = {result['return_time']}\n\n"

        f"Для {device_type} в расчёте использована величина расхода: "
        f"{result['consumption_label']}.\n\n"

        "Расчёт выполнен по формулам Приложения № 3 "
        "к Приказу МЧС России от 27.06.2022 № 640."
    )


def send_formulas(vk, user_id):
    message = (
        "📖 Формулы расчёта параметров работы в СИЗОД\n\n"
        "Источник: Приложение № 3 к Приказу МЧС России "
        "от 27.06.2022 № 640.\n\n"
        "1. Pmax.пад = Pmin.вкл / 3\n\n"
        "2. Pк.вых = Pmin.вкл - Pmax.пад\n\n"
        "3. ΔT для ДАСВ = Pmax.пад × Vб / 45\n\n"
        "4. ΔT для ДАСК = Pmax.пад × Vб / 2\n\n"
        "5. Tвых = Tвкл + ΔT\n\n"
        "6. Tобщ для ДАСВ = Pmin.вкл × Vб / 45\n\n"
        "7. Tобщ для ДАСК = Pmin.вкл × Vб / 2\n\n"
        "8. Tвозвр = Tвкл + Tобщ"
    )

    send_message(
        vk=vk,
        user_id=user_id,
        message=message
    )