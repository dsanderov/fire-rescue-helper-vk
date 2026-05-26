def calculate_free_fire_development(
    aps_present,
    travel_time,
    deployment_time
):
    if aps_present:
        detection_message_time = 5
    else:
        detection_message_time = 10

    alarm_assembly_time = 1

    total_time = (
        detection_message_time
        + alarm_assembly_time
        + travel_time
        + deployment_time
    )

    return {
        "aps_present": aps_present,
        "detection_message_time": detection_message_time,
        "alarm_assembly_time": alarm_assembly_time,
        "travel_time": travel_time,
        "deployment_time": deployment_time,
        "total_time": total_time
    }