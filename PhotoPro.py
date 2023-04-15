import os
import requests
from pyrogram import Client, filters
import time
from pyrocon import patch
import datetime
import configparser



config = configparser.ConfigParser()
config.read("config.ini")
api_id = config['@Vilas_Photography']['api_id']
api_hash = config['@Vilas_Photography']['api_hash']
bot_token = config['@Vilas_Photography']['token']
COTOUT_KEY =  config['@Vilas_Photography']['cotout_key']


app = Client(
  "PhotoPro",
  api_id=api_id,
  api_hash=api_hash,
  bot_token=bot_token,
)

quiz = patch(app, clear=True)

API_KEY = COTOUT_KEY

mess = """
Hi {} {}! Welcome to our PhotoPro editing bot 📷!

This bot is created by @Vilas_Photography to help you enhance your photos with various filters and effects..

**Type** /edit  To Start Editing"""

msg = (
  "Here's what you can do with our bot:\n\n"
  f"- /removebackground - **To Remove Background of Photo.**\n\n"
  f"- /facecut - **To Cut the face from photo.**\n\n"
  f"- /enhancephoto - **To enhance Photo.** (Recommended to use this feature before using all features)\n\n"
  f"- /colorizephoto - **To colorize Photo.**\n\n"
  f"- /cartoonifyphoto - **To make cartoon of Photo**.\n\n"
  f"- /colorcorrection - **To correct color of Photo.**\n\n")


@app.on_message(filters.command("removebackground"))
async def removebackground(bot, message):
  print('remove background')
  
  answer = await quiz.ask(message,
                          "Please send the photo to remove background from:",
                          filter=(filters.photo))
  photo = answer.photo.file_id
  file_path = await app.download_media(photo)
  now = datetime.datetime.now()
  filename = now.strftime("%Y-%m-%d_%H-%M-%S")
  response = requests.post(
    "https://www.cutout.pro/api/v1/matting?mattingType=6",
    files={"file": open(file_path, "rb")},
    headers={"APIKEY": API_KEY},
  )

  with open(f"{filename}.png", "wb") as out:
    out.write(response.content)
  await bot.send_photo(message.chat.id, open(f"{filename}.png", "rb"))
  os.remove(f"{filename}.png")
  os.remove(file_path)
  await bot.send_message(message.chat.id, msg)


@app.on_message(filters.command("facecut"))
async def facecut(bot, message):
  print(f'face cut')
  answer = await quiz.ask(message,
                          "Please send the photo to cut the face from:",
                          filter=(filters.photo))
  photo = answer.photo.file_id
  file_path = await app.download_media(photo)
  now = datetime.datetime.now()
  filename = now.strftime("%Y-%m-%d_%H-%M-%S")
  response = requests.post(
    "https://www.cutout.pro/api/v1/matting?mattingType=3",
    files={"file": open(file_path, "rb")},
    headers={"APIKEY": API_KEY},
  )
  with open(f"{filename}.png", "wb") as out:
    out.write(response.content)
  await bot.send_photo(message.chat.id, open(f"{filename}.png", "rb"))
  os.remove(f"{filename}.png")
  os.remove(file_path)
  await bot.send_message(message.chat.id, msg)


@app.on_message(filters.command("enhancephoto"))
async def enhancephoto(bot, message):
  print(f'enhance photo')
  answer = await quiz.ask(message,
                          "Please send the photo to enhance:",
                          filter=(filters.photo))
  photo = answer.photo.file_id
  file_path = await app.download_media(photo)
  now = datetime.datetime.now()
  filename = now.strftime("%Y-%m-%d_%H-%M-%S")
  response = requests.post(
    "https://www.cutout.pro/api/v1/matting?mattingType=18",
    files={"file": open(file_path, "rb")},
    headers={"APIKEY": API_KEY},
  )

  with open(f"{filename}.png", "wb") as out:
    out.write(response.content)
  await bot.send_photo(message.chat.id, open(f"{filename}.png", "rb"))
  os.remove(f"{filename}.png")
  os.remove(file_path)
  await bot.send_message(message.chat.id, msg)


@app.on_message(filters.command("cartoonifyphoto"))
async def start_cartoonifyphoto(bot, message):
  print(f'cartoonify photo')
  await bot.send_message(message.chat.id, "Please select a cartoon type:")

  await bot.send_photo(
    message.chat.id,
    "https://d38b044pevnwc9.cloudfront.net/cutout-nuxt/cartoon/cartoonFace/type09.jpg",
    caption="/cartoonifyphoto9")
  await bot.send_photo(
    message.chat.id,
    "https://d38b044pevnwc9.cloudfront.net/cutout-nuxt/cartoon/cartoonFace/9.jpg",
    caption="/cartoonifyphoto8")
  await bot.send_photo(
    message.chat.id,
    "https://d38b044pevnwc9.cloudfront.net/cutout-nuxt/cartoon/cartoonFace/8.jpg",
    caption="/cartoonifyphoto7")
  await bot.send_photo(
    message.chat.id,
    "https://d38b044pevnwc9.cloudfront.net/cutout-nuxt/cartoon/cartoonFace/7.jpg",
    caption="/cartoonifyphoto6")
  await bot.send_photo(
    message.chat.id,
    "https://d38b044pevnwc9.cloudfront.net/cutout-nuxt/cartoon/cartoonFace/1.jpg",
    caption="/cartoonifyphoto5")
  await bot.send_photo(
    message.chat.id,
    "https://d38b044pevnwc9.cloudfront.net/cutout-nuxt/cartoon/cartoonFace/2.jpg",
    caption="/cartoonifyphoto4")
  await bot.send_photo(
    message.chat.id,
    "https://d38b044pevnwc9.cloudfront.net/cutout-nuxt/cartoon/cartoonFace/6.jpg",
    caption="/cartoonifyphoto3")
  await bot.send_photo(
    message.chat.id,
    "https://d38b044pevnwc9.cloudfront.net/cutout-nuxt/cartoon/cartoonFace/5.jpg",
    caption="/cartoonifyphoto2")
  await bot.send_photo(
    message.chat.id,
    "https://d38b044pevnwc9.cloudfront.net/cutout-nuxt/cartoon/cartoonFace/4.jpg",
    caption="/cartoonifyphoto1")
  await bot.send_photo(
    message.chat.id,
    "https://d38b044pevnwc9.cloudfront.net/cutout-nuxt/cartoon/cartoonFace/3.jpg",
    caption="/cartoonifyphoto0")

  @app.on_message(filters.regex("^/cartoonifyphoto\d+$"))
  async def receive_cartoon_type(bot, message):
    print(message.text)
    cartoonType = int(message.text[len("/cartoonifyphoto"):])
    print("cartoonType =", cartoonType)
    answer = await quiz.ask(message, "send a photo", filter=(filters.photo))
    photo = answer.photo.file_id
    file_path = await app.download_media(photo)
    now = datetime.datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M-%S")
    response = requests.post(
      f"https://www.cutout.pro/api/v1/cartoonSelfie?cartoonType={cartoonType}",
      files={"file": open(file_path, "rb")},
      headers={"APIKEY": API_KEY},
    )
    with open(f"{filename}.png", "wb") as out:
      out.write(response.content)
    await bot.send_photo(message.chat.id, open(f"{filename}.png", "rb"))
    os.remove(f"{filename}.png")
    os.remove(file_path)
    await bot.send_message(message.chat.id, msg)


@app.on_message(filters.command("colorcorrection"))
async def colorcorrection(bot, message):
  print('color correction')
  answer = await quiz.ask(message,"Please send the photo for color correction:",filter=(filters.photo))
  photo = answer.photo.file_id
  file_path = await app.download_media(photo)
  now = datetime.datetime.now()
  filename = now.strftime("%Y-%m-%d_%H-%M-%S")
  response = requests.post(
    "https://www.cutout.pro/api/v1/matting?mattingType=4",
    files={"file": open(file_path, "rb")},
    headers={"APIKEY": API_KEY},
  )

  with open(f"{filename}.png", "wb") as out:
    out.write(response.content)
  await bot.send_photo(message.chat.id, open(f"{filename}.png", "rb"))
  os.remove(f"{filename}.png")
  os.remove(file_path)
  await bot.send_message(message.chat.id, msg)


@app.on_message(filters.command("colorizephoto"))
async def process_photo(bot, message):
  print('Colorize Photo')
  answer = await quiz.ask(message,
                          "Please send the photo to colorize:",
                          filter=(filters.photo))
  photo = answer.photo.file_id
  file_path = await app.download_media(photo)
  now = datetime.datetime.now()
  filename = now.strftime("%Y-%m-%d_%H-%M-%S")
  response = requests.post(
    "https://www.cutout.pro/api/v1/matting?mattingType=19",
    files={"file": open(file_path, "rb")},
    headers={"APIKEY": API_KEY},
  )

  with open(f"{filename}.png", "wb") as out:
    out.write(response.content)
  await bot.send_photo(message.chat.id, open(f"{filename}.png", "rb"))
  os.remove(f"{filename}.png")
  os.remove(file_path)
  await bot.send_message(message.chat.id, msg)





    


@app.on_message(filters.command("start"))
async def start(bot, message):
  await bot.send_message(
    message.chat.id,
    mess.format(message.chat.first_name, message.chat.last_name))


app.run()
