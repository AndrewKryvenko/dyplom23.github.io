import asyncio
import json

from aiogram import types
from aiogram import Bot, Dispatcher
from aiogram.types import WebAppEvent

bot = Bot(token="6442089419:AAG4q9RlLlpJ7w4HEKusOqTXUA18MSMaK_w")
dp = Dispatcher(bot)

@dp.web_app_message_handler()
async def process_order(event: WebAppEvent):
    json_data = event.data
    parsed_data = json.loads(json_data)
    
    message_text = ""
    for i, item in enumerate(parsed_data['items'], start=1):
        position = int(item['id'].replace('item', ''))
        message_text += f"Позиція {position}\n"
        message_text += f"Вартість {item['price']}\n\n"
        message_text += f"Кількість {item['quantity']}\n\n"

    message_text += f"Загальна вартість: {parsed_data['totalPrice']}"

    # Отправляем сообщение о заказе в чат с клиентом
    await bot.send_message(event.from_user.id, message_text)
    
    # Отправляем сообщение о заказе в отдельный чат
    await bot.send_message('-1002022582711', f"Нове замовлення\n{message_text}")


async def main():
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
