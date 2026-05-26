from handlers.first_aid.first_aid_menu import (
    handle_first_aid_menu
)

from handlers.first_aid.unconscious_person import (
    handle_unconscious_person
)

from handlers.first_aid.no_breathing_cpr import (
    handle_no_breathing_cpr
)

from handlers.first_aid.bleeding import (
    handle_bleeding
)

from handlers.first_aid.carbon_monoxide import (
    handle_carbon_monoxide
)

from handlers.first_aid.electrical_injury import (
    handle_electrical_injury
)

from handlers.first_aid.burns import (
    handle_burns
)

from handlers.first_aid.fractures import (
    handle_fractures
)

from handlers.first_aid.frostbite import (
    handle_frostbite
)

from handlers.first_aid.shock import (
    handle_shock
)

from handlers.first_aid.foreign_body_airway import (
    handle_foreign_body_airway
)

from handlers.first_aid.triage import (
    handle_triage
)


def handle_first_aid_router(vk, user_id, text):
    if text == "🩺 первая помощь":
        handle_first_aid_menu(vk, user_id)
        return True

    if text == "🚫 нет сознания":
        handle_unconscious_person(vk, user_id)
        return True

    if text == "🫁 нет дыхания / слр":
        handle_no_breathing_cpr(vk, user_id)
        return True

    if text == "🩸 кровотечение":
        handle_bleeding(vk, user_id)
        return True

    if text == "🔥 ожоги":
        handle_burns(vk, user_id)
        return True

    if text == "🧊 обморожения":
        handle_frostbite(vk, user_id)
        return True

    if text == "☠ отравление co":
        handle_carbon_monoxide(vk, user_id)
        return True

    if text == "⚡ электротравма":
        handle_electrical_injury(vk, user_id)
        return True

    if text == "🦴 переломы":
        handle_fractures(vk, user_id)
        return True

    if text == "🫀 шок":
        handle_shock(vk, user_id)
        return True

    if text == "🫁 инородное тело":
        handle_foreign_body_airway(vk, user_id)
        return True

    if text == "🚑 сортировка":
        handle_triage(vk, user_id)
        return True

    return False