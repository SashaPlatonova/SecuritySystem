import config
import telebot
from telebot import types
import logging
import datetime
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import requests
import os

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)  # Outputs debug messages to console.

bot = telebot.TeleBot(config.token, threaded=True)

### Функция проверки авторизации
def autor(chatid):
    strid = str(chatid)
    for item in config.users:
        if item == strid:
            return True
    return False

### Функция массвой рассылки уведомлений
def sendall(text):
    if len(config.users) > 0:
        for user in config.users:
            try:
                bot.send_message(user, text)
            except:
                print(str(datetime.datetime.now()) + ' ' + 'Ошибка отправки сообщения ' + text + ' пользователю ' + str(
                    user))

### Функция проверки режима
def checkmode():
    try:
        mode_file = open("mode.txt", "r")
        modestring = mode_file.read()
        mode_file.close()
        if modestring == '1':
            return True
        else:
            return False
    except:
        return False

print(str(datetime.datetime.now()) + ' ' + 'Start watching')
sendall(str(datetime.datetime.now()) + ' ' + 'Start watching')

### Главное меню
@bot.message_handler(commands=['Меню', 'start', 'Обновить'])
def menu(message):
    
    if autor(message.chat.id):
        markup = types.ReplyKeyboardMarkup()
        markup.row('/Обновить', '/Охрана')
        if checkmode():
            bot.send_message(message.chat.id, 'Режим охраны ВКЛ.', reply_markup=markup)
        #else:
            #bot.send_message(message.chat.id, 'Режим охраны ВЫКЛ.', reply_markup=markup)
        try:
            
            f = open("image.jpg", 'rb')
            f_name = open("name.txt", 'r')
            bot.send_photo(message.chat.id, f)
            msg = f_name.readline()
            if msg == "unknown":
                bot.send_message(message.chat.id, msg + " is doing something fishy")
            else:
                bot.send_message(message.chat.id, msg + " has come to you")
        except:
            bot.send_message(message.chat.id, 'Фоток нет')
    else:
        markup = types.ReplyKeyboardMarkup()
        markup.row('/Обновить')
        bot.send_message(message.chat.id, 'Тебе сюда нельзя. Твой ID: ' + str(message.chat.id), reply_markup=markup)

### Смена режима
@bot.message_handler(commands=['Охрана'])
def toggle(message):
    if autor(message.chat.id):
        try:
            if checkmode():
                last_file = open("mode.txt", "w")
                last_file.write('0')
                last_file.close()
                sendall('Пользователь ' + message.chat.first_name + ' выключил режим охраны')
            else:
                last_file = open("mode.txt", "w")
                last_file.write('1')
                last_file.close()
                sendall('Пользователь ' + message.chat.first_name + ' включил режим охраны')
                while checkmode():
                    try:
            
                        f = open("image.jpg", 'rb')
                        f_name = open("name.txt", 'r')
                        bot.send_photo(message.chat.id, f)
                        msg = f_name.readline()
                        if msg == "unknown":
                            bot.send_message(message.chat.id, msg + " is doing something fishy")
                        else:
                            bot.send_message(message.chat.id, msg + " has come to you")
                        time.sleep(7)
                    except:
                        time.sleep(1)#bot.send_message(message.chat.id, 'Фоток нет')
                    
        except:
            bot.send_message(message.chat.id, 'Mode change error')
            print(str(datetime.datetime.now()) + ' ' + "Mode change error")
        menu(message)

if __name__ == '__main__':
    
   
    bot.polling(none_stop=False)
    last_file = open("mode.txt", "w")
    last_file.write('0')
    last_file.close()
    os.remove("image.jpg")
    os.remove("name.txt")
    
