import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from config import TOKEN
from router import route_message
from services.navigation.register_menus import register_all_menus


vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

register_all_menus()

print("Бот запущен")


for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me:

        user_id = event.user_id
        text = event.text.lower()

        print(f"[НОВОЕ СООБЩЕНИЕ] {text}")

        route_message(vk, user_id, text)