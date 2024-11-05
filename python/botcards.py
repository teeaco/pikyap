import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = "7322283656:AAEMQT40skWKrNKATIR5mMLBiqsM1Bgj3zY"
bot = telebot.TeleBot(token)

folders = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Создать папку", callback_data="create_folder"))
    markup.add(InlineKeyboardButton("Показать папки", callback_data="list_folders"))
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите действие:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "create_folder")
def create_folder_prompt(call):
    msg = bot.send_message(call.message.chat.id, "Введите название новой папки:")
    bot.register_next_step_handler(msg, create_folder)

def create_folder(message):
    folder_name = message.text
    if folder_name:
        folders[folder_name] = []
        bot.send_message(message.chat.id, f"Папка '{folder_name}' создана.")
    else:
        bot.send_message(message.chat.id, "Имя папки не может быть пустым.")

@bot.callback_query_handler(func=lambda call: call.data == "list_folders")
def list_folders(call):
    if not folders:
        bot.send_message(call.message.chat.id, "Нет созданных папок.")
    else:
        markup = InlineKeyboardMarkup()
        for folder in folders:
            markup.add(InlineKeyboardButton(folder, callback_data=f"open_folder_{folder}"))
        bot.send_message(call.message.chat.id, "Выберите папку:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("open_folder_"))
def open_folder(call):
    folder_name = call.data.split("_")[2]
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Добавить карточку", callback_data=f"add_card_{folder_name}"))
    markup.add(InlineKeyboardButton("Просмотреть карточки", callback_data=f"view_cards_{folder_name}"))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=f"Папка: {folder_name}", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("add_card_"))
def add_card_prompt(call):
    folder_name = call.data.split("_")[2]
    msg = bot.send_message(call.message.chat.id, "Введите текст карточки:")
    bot.register_next_step_handler(msg, add_card, folder_name)

def add_card(message, folder_name):
    card_text = message.text
    if folder_name in folders:
        folders[folder_name].append(card_text)
        bot.send_message(message.chat.id, f"Карточка добавлена в папку '{folder_name}'.")

@bot.callback_query_handler(func=lambda call: call.data.startswith("view_cards_"))
def view_cards(call):
    folder_name = call.data.split("_")[2]
    if folder_name in folders and folders[folder_name]:
        cards = "\n".join(f"- {card}" for card in folders[folder_name])
        bot.send_message(call.message.chat.id, f"Карточки в папке '{folder_name}':\n{cards}")
    else:
        bot.send_message(call.message.chat.id, f"В папке '{folder_name}' пока нет карточек.")

# Запуск бота
print("Бот запущен")
bot.polling()
