#https://my.telegram.org/apps
#Instagram syscursos
#Telegram t.me/syscursos

from telethon import TelegramClient, events
import apiData
from datetime import datetime
import pyjokes

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
joke = pyjokes.get_joke(language='es', category='all')


client = TelegramClient('session', apiData.api_id, apiData.api_hash)

@client.on(events.NewMessage(chats=apiData.chatName))

async def my_event_handler(event):

  respuesta = answer(event.text)
  print(event.text)
  await client.send_message(apiData.chatName, respuesta)

def answer(word):
      
  if word == '/broma':
      return joke
  
  if word == '/hora':
      return current_time

client.start()
client.run_until_disconnected()

