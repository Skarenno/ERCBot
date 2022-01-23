import os
import random
import time
import datetime	
from threading import Timer
import schedule
import telebot
from telegram import message
from threading import Thread
from time import sleep

dict = {
    1 : "AO MANCANO ",
    2 : "SBORRA ASSOLUTA TRA ",
    3 : ""
}

#CENTRASSINO TOKEN ID --> -303561414
Bot = telebot.TeleBot("5156138857:AAFvOH6DR7dny3pV3ghQr4W7txbyGgN3WO4")

def countdown(stop) -> str:
    while True:
        difference = stop - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            #
            break
        print('The count is: '
              + str(difference.days) + " day(s) "
              + str(count_hours) + " hour(s) "
              + str(count_minutes) + " minute(s) "
              + str(count_seconds) + " second(s) "
              )
        time.sleep(1)
        return str(difference.days)

end_time = datetime.datetime(2022, 2, 25, 00, 00, 0)
countdown(end_time)

updates = Bot.get_updates(1, 100, 20)
print(updates)


@Bot.message_handler(commands=['update', 'help'])
def update(message):
    days = countdown(end_time)
    key = random.choice(list(dict.keys()))
    if(key == 3):
        Bot.reply_to(message, "TRA " + days + " GIORNI SI SBOCCIA")
    else:
        Bot.reply_to(message, dict.get(key) + days + " GIORNI")

@Bot.message_handler(commands=['updatetitle'])
def updatetitle(message):
    days = countdown(end_time)
    Bot.set_chat_title("-303561414", "Centrassino 2022 -" + days)
    
def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def AutomaticMidnightUpdate():
    days = countdown(end_time)
    Bot.send_message("-303561414", "MEZZANOTTE DIOCANE")
    Bot.set_chat_title("-303561414", "Centrassino 2022 -" + days)

if __name__ == "__main__":
    # Creating the jon for scheduling in thread
    schedule.every().day.at("20:06").do(AutomaticMidnightUpdate)

    #Thread to not block the bot
    Thread(target=schedule_checker).start() 


Bot.infinity_polling()