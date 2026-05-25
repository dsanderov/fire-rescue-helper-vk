from datetime import datetime, timedelta


def calculate_gdzs_air(
    device_type,
    p_min,
    cylinder_volume,
    start_time
):
    p_max_drop = p_min / 3
    p_exit = p_min - p_max_drop

    if device_type == "ДАСВ":
        delta_time = (p_max_drop * cylinder_volume) / 45
        total_time = (p_min * cylinder_volume) / 45

    elif device_type == "ДАСК":
        delta_time = (p_max_drop * cylinder_volume) / 2
        total_time = (p_min * cylinder_volume) / 2

    else:
        raise ValueError("Неизвестный тип СИЗОД")

    exit_command_time = add_minutes_to_time(
        start_time,
        delta_time
    )

    return_time = add_minutes_to_time(
        start_time,
        total_time
    )

    return {
        "device_type": device_type,
        "p_min": p_min,
        "cylinder_volume": cylinder_volume,
        "start_time": start_time,
        "p_max_drop": p_max_drop,
        "p_exit": p_exit,
        "delta_time": delta_time,
        "exit_command_time": exit_command_time,
        "total_time": total_time,
        "return_time": return_time
    }


def add_minutes_to_time(time_text, minutes):
    base_time = datetime.strptime(time_text, "%H:%M")
    result_time = base_time + timedelta(minutes=minutes)

    return result_time.strftime("%H:%M")