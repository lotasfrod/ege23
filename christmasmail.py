import telebot
import random
from telebot import types

gifts = ['Cake Bonch', 'Bonch Luv', 'OG Bruevich', 'Bushido Bonch', '163ONMYBONCH', 'THRILL BONCH', 'Dj bonch', 'BONCH.Fludd', 'BONCHSHTERN', 'Slava Bruevich', 'Каспийский Бонч', 'BONCHBLAK 52', 'FRINDLY THUG 52 NGG', 'Big Russian Bonch', 'Big Baby Bonch', 'A$ap Bonch', 'Lil Bruevich', 'Lil Uzi Bonch', '21 Bruevich', 'Boulevard Bonch', 'три дня бонча']

bot = telebot.TeleBot('6394041496:AAGm98QShd4ZUGI0bgVyFibqcD7sbQe8l_8')


@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Утешение")
        item3=types.KeyboardButton("Музыкальный исполнитель")
        item4 = types.KeyboardButton('Пожелание')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(m.chat.id, 'Нажми: \n\nФакт - для получения интересного факта\n\nУтешение — для получения мудрой цитаты\n\nМузыкальный исполнитель - для получения одного из авторов прекрасной современной музыки\n\nПожелание - для получения пожелания.',  reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Факт' :
            answer = 'Ты сделал правильный выбор!'
    elif message.text.strip() == 'Утешение':
            answer = 'Всё будет Бонч-Бруевич'
    elif message.text.strip() == 'Музыкальный исполнитель':
            answer = random.choice(gifts)
    else:
            answer = 'https://youtu.be/CViks8-yUT4'

    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True, interval=0)