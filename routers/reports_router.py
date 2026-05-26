from handlers.reports.reports_menu import (
    handle_reports_menu
)

from handlers.reports.arrival_report import (
    handle_arrival_report_start,
    handle_arrival_report_router
)


def handle_reports_router(vk, user_id, text):
    if text == "📡 доклады":
        handle_reports_menu(vk, user_id)
        return True

    if text == "🚒 доклад по прибытии":
        handle_arrival_report_start(vk, user_id)
        return True

    if handle_arrival_report_router(
        vk,
        user_id,
        text
    ):
        return True

    return False