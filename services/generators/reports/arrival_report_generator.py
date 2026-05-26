def generate_arrival_report(data):
    address = data["address"]
    object_type = data["object_type"]
    fire_signs = data["fire_signs"]
    burning = data["burning"]
    fire_place = data["fire_place"]
    people_threat = data["people_threat"]
    forces = data["forces"]
    actions = data["actions"]
    additional = data["additional"]
    characteristics = data.get("characteristics")

    report = (
        "📡 Доклад по прибытии\n\n"

        "ЦППС, докладывает РТП-1.\n\n"

        f"Прибыли на место: {address}.\n"
    )

    if characteristics:
        report += (
            f"Объект: {characteristics}.\n"
        )
    else:
        report += (
            f"Объект: {object_type}.\n"
        )

    report += (
        f"По внешним признакам: {fire_signs}.\n"
        f"Предварительно горит: {burning}.\n"
        f"Место пожара: {fire_place}.\n\n"

        f"Угроза людям: {people_threat}.\n"
        f"На месте: {forces}.\n"
        f"Проводимые действия: {actions}.\n"
        f"Дополнительно требуется: {additional}.\n\n"

        "Дальнейшая разведка"
    )

    return report