from handlers.checklists.checklists_menu import (
    handle_checklists_menu
)

from handlers.checklists.fire_recon import (
    handle_fire_recon_checklist
)


def handle_checklists_router(vk, user_id, text):
    if text == "📋 чек-листы":
        handle_checklists_menu(vk, user_id)
        return True

    if text == "🔍 разведка пожара":
        handle_fire_recon_checklist(vk, user_id)
        return True

    return False