from telethon import TelegramClient, sync
import openpyxl

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
phone = 'YOUR_PHONE_NUMBER'

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone)

chat_id = YOUR_CHAT_ID
members = client.get_participants(chat_id)

wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Имя", "ID", "Username"])

for member in members:
    ws.append([member.first_name, member.id, member.username])

wb.save("members.xlsx")
