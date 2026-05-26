from handlers.menu import handle_main_menu

from services.navigation.navigation import (
    go_back,
    reset_navigation
)

from services.navigation.menu_actions import (
    open_registered_menu
)

from services.messages.sender import send_message

from services.states.state_manager import (
    clear_state
)

from routers.main_router import handle_main_router

from routers.situations_router import (
    handle_situations_router
)

from routers.calculators.gdzs_router import (
    handle_gdzs_router
)

from routers.calculators.free_development_router import (
    handle_free_development_router
)

from routers.first_aid_router import (
    handle_first_aid_router
)

from routers.reports_router import (
    handle_reports_router
)

from routers.checklists_router import (
    handle_checklists_router
)


def route_message(vk, user_id, text):

    if text in ["⬅ главное меню", "❌ отмена"]:

        clear_state(user_id)

        reset_navigation(user_id)

        handle_main_menu(vk, user_id)

        return

    if text == "⬅ назад":
        previous_menu = go_back(user_id)

        if previous_menu is None:
            open_registered_menu(
                vk,
                user_id,
                "main_menu"
            )

            return

        if open_registered_menu(
            vk,
            user_id,
            previous_menu
        ):
            return

        open_registered_menu(
            vk,
            user_id,
            "main_menu"
        )

        return

    if handle_main_router(vk, user_id, text):
        return

    if handle_situations_router(vk, user_id, text):
        return

    if handle_gdzs_router(vk, user_id, text):
        return

    if handle_free_development_router(vk, user_id, text):
        return

    if handle_first_aid_router(vk, user_id, text):
        return

    if handle_reports_router(vk, user_id, text):
        return

    if handle_checklists_router(vk, user_id, text):
        return

    send_message(
        vk=vk,
        user_id=user_id,
        message="❌ Неизвестная команда."
    )