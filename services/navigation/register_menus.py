from services.navigation.menu_registry import register_menu

from handlers.menu import handle_main_menu

from handlers.situations.situations_menu import (
    handle_situations_menu
)

from handlers.calculators.calculators_menu import (
    handle_calculators_menu
)

from handlers.calculators.gdzs.gdzs_menu import (
    handle_gdzs_menu
)

from handlers.first_aid.first_aid_menu import (
    handle_first_aid_menu
)


def register_all_menus():
    register_menu("main_menu", handle_main_menu)
    register_menu("situations_menu", handle_situations_menu)
    register_menu("calculators_menu", handle_calculators_menu)
    register_menu("gdzs_menu", handle_gdzs_menu)
    register_menu("first_aid_menu", handle_first_aid_menu)