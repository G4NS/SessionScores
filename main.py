import telebot
from config import *
bot = telebot.TeleBot(bot_api) #token

@bot.message_handler(commands=["start"])
def start(message):
    if(id != message.chat.id):
        bot.send_message(id, f"===BOT STARTED, command=start==\nid-{message.chat.id}\nusername-{message.chat.username}\nlast name-{message.chat.last_name}\nname-{message.chat.first_name}")
    bot.send_message(message.chat.id, f"Привет, {message.chat.first_name}\n\n/info - Узнать сколько баллов что дает \n/calc - Рассчитать сколько баллов надо")

@bot.message_handler(commands=["menu"])
def start(message):
    if(id != message.chat.id):
        bot.send_message(id, f"===BOT STARTED, command=menu==\nid-{message.chat.id}\nusername-{message.chat.username}\nlast name-{message.chat.last_name}\nname-{message.chat.first_name}")
    bot.send_message(message.chat.id, "/info - Узнать сколько баллов что дает \n/calc - Рассчитать сколько баллов надо")

@bot.message_handler(commands=["info"])
def info(message):
    if (id != message.chat.id):
        bot.send_message(id,f"===BOT STARTED, command=info==\nid-{message.chat.id}\nusername-{message.chat.username}\nlast name-{message.chat.last_name}\nname-{message.chat.first_name}")
    bot.send_message(message.chat.id, "Формула для расчета баллов: \n(1рк + 2рк + 3рк) * 0.2 + session * 0.4\n\n0-24 - Лето\n25-49 - Пересдача 7,5к тг\n50-69 - Норм, но без степухи\n70-89 - Хорошо\n90-100 - Пятерка")

@bot.message_handler(commands=["calc"])
def calc(message):
    if (id != message.chat.id):
        bot.send_message(id, f"===BOT STARTED, command=calc==\nid-{message.chat.id}\nusername-{message.chat.username}\nlast name-{message.chat.last_name}\nname-{message.chat.first_name}")
    buffer = bot.send_message(message.chat.id, "1 - РК:")
    bot.register_next_step_handler(buffer, RK1)

def RK1(message):
    global rk_1
    rk_1 = message.text
    if(rk_1.isdigit()):
        rk_1 = int(message.text)

        if(rk_1 >= 0 and rk_1 <= 100):
            buffer = bot.send_message(message.chat.id, "2 - РК:")
            bot.register_next_step_handler(buffer, RK2)
        else:
            bot.send_message(message.chat.id, "В диапазоне от 0 до 100!\n/calc")
    else:
        bot.send_message(message.chat.id, "Только целочисленные цифры!\n/calc")

def RK2(message):
    global rk_2
    rk_2 = message.text
    if (rk_2.isdigit()):
        rk_2 = int(message.text)

        if(rk_2 >= 0 and rk_2 <= 100):
            buffer = bot.send_message(message.chat.id, "3 - РК:")
            bot.register_next_step_handler(buffer, RK3)
        else:
            bot.send_message(message.chat.id, "В диапазоне от 0 до 100!\n/calc")
    else:
        bot.send_message(message.chat.id, "Только целочисленные цифры!\n/calc")

def RK3(message):
    global rk_3
    rk_3 = message.text

    if(rk_3.isdigit()):
        rk_3 = int(message.text)

        if(rk_3 >= 0 and rk_3 <= 100):
            rk = float((rk_1 + rk_2 + rk_3)) * 0.2
            stepuxa = (70 - rk) / 0.4
            povishka = (90 - rk) / 0.4
            bot.send_message(message.chat.id, f"Для стипендии надо набрать: {stepuxa}")
            if povishka <= 100:
                bot.send_message(message.chat.id, f"Для повышки надо набрать: {povishka}")
            else:
                bot.send_message(message.chat.id, "Нету шанса на повышку)")
        else:
            bot.send_message(message.chat.id, "В диапазоне от 0 до 100!\n/calc")
    else:
        bot.send_message(message.chat.id, "Только целочисленные цифры!\n/calc")

try:
    bot.polling(none_stop=True)
except:
    pass