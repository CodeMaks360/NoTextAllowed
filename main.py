import discord
import os

Client = discord.Client()

whitelistP = ["png", "gif", "jpg", "jpeg", "bmp"] #whitelist for pictures
whitelistV = ["mp4", "mov", "webm", "m4p", ".mpg", ".mpeg", ".m2v", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv"] #whitelist for videos

@Client.event
async def on_ready():
    print('Logged as {0.user}'.format(Client))

@Client.event
async def on_message(message):
  message.content = message.content.lower()
  if message.author == Client.user:
    return

  if str(message.channel) == "images": #pictures channel onyl
    if not message.attachments:
      await message.channel.purge(limit = 1)

    for attachment in message.attachments:
      if attachment.filename.split('.')[-1] not in whitelistP:
        await message.channel.purge(limit = 1)
  
  elif str(message.channel) == "movies": #videos channel onyl
    if not message.attachments:
      await message.channel.purge(limit = 1)

    for attachment in message.attachments:
       if attachment.filename.split('.')[-1] not in whitelistV:
        await message.channel.purge(limit = 1)

Client.run(os.getenv('TOKEN')) #get bot's token from .env file
