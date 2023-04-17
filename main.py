from telethon import TelegramClient, sync
import openpyxl

api_id = api
api_hash = 'api_hash'
phone = 'phone'
chat_id = chat_id


client = TelegramClient('session_name', api_id, api_hash)
client.start(phone)

members = client.get_participants(chat_id)

wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Имя", "ID", "Username"])

for member in members:
    ws.append([member.first_name, member.id, member.username])

wb.save("members.xlsx")
