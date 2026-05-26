from datetime import datetime, timedelta
import math


DASV_AIR_CONSUMPTION = 45
DASK_OXYGEN_CONSUMPTION = 2


def calculate_gdzs_air(
    device_type,
    p_min,
    cylinder_volume,
    start_time
):
    p_max_drop = p_min / 3
    p_exit = p_min - p_max_drop

    if device_type == "ДАСВ":
        divisor = DASV_AIR_CONSUMPTION
        consumption_label = "45 л/мин"

    elif device_type == "ДАСК":
        divisor = DASK_OXYGEN_CONSUMPTION
        consumption_label = "2 л/мин"

    else:
        raise ValueError("Неизвестный тип СИЗОД")

    delta_time = (p_max_drop * cylinder_volume) / divisor
    total_time = (p_min * cylinder_volume) / divisor

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
        "total_time": total_time,
        "exit_command_time": exit_command_time,
        "return_time": return_time,
        "divisor": divisor,
        "consumption_label": consumption_label
    }


def add_minutes_to_time(time_text, minutes):
    base_time = datetime.strptime(time_text, "%H:%M")

    rounded_minutes = round_minutes(minutes)

    result_time = base_time + timedelta(
        minutes=rounded_minutes
    )

    return result_time.strftime("%H:%M")


def round_minutes(minutes):
    return math.floor(minutes + 0.5)