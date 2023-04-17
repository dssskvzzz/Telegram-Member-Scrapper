from telethon import TelegramClient, sync
import openpyxl

# Ваши учетные данные API
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
phone = 'YOUR_PHONE_NUMBER'

# Создание объекта клиента Telegram
client = TelegramClient('session_name', api_id, api_hash)

# Аутентификация пользователя
client.start(phone)

# Получение списка участников чата
chat_id = YOUR_CHAT_ID
members = client.get_participants(chat_id)

# Запись участников в файл Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Имя", "ID", "Username"])

for member in members:
    ws.append([member.first_name, member.id, member.username])

wb.save("members.xlsx")
