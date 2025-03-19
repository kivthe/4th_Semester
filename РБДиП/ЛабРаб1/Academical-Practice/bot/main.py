import telebot
import json
import requests

import util

#------------------------------------------------------------

backend_address = '127.0.0.1'
backend_port = 8000

TOKEN = '7250335892:AAHBT8EkT9cFwEN6gQXwXwPxMaonkBY-kCc'
bot = telebot.TeleBot(TOKEN)

#------------------------------------------------------------

@bot.message_handler(commands=["start"])
def main(message):
  bot.send_message(message.chat.id, 'Приветсвую!')

#------------------------------------------------------------

@bot.message_handler(commands=["about"])
def main(message):
  bot.send_message(message.chat.id, '''Я - бот для поиска и фильтрации вакансий с помощью API сайта Head Hunter.
Мой создатель - Игорь Кузнецов (@kivthe)''')

#------------------------------------------------------------

@bot.message_handler(commands=["help"])
def main(message):
  bot.send_message(message.chat.id, '''start - Начало работы с ботом
about - Вывод информации про бота
help - Вывод вспомогательной информации о командах бота      
knock - \"Постучаться\", узнать, работает ли сейчас сервер, или нет       
refresh - Создание запроса на сервер об обновлении и добавлении новых данных о вакансиях
query - Запросить данные с сервера''')

#------------------------------------------------------------

@bot.message_handler(commands=["knock"])
def main(message):
  if util.CanConnect(backend_address, backend_port):
    bot.send_message(message.chat.id, 'Сервер сейчас онлайн!')
  else:
    bot.send_message(message.chat.id, 'Сервер сейчас оффлайн!')

#------------------------------------------------------------

@bot.message_handler(commands=["get"])
def main(message):
  bot.send_message(message.chat.id, '''Введите свои параметры команды через запятую:
Минимальну зарплату, валюту зарплаты и необходимый опты работы (в годах)
Например: 1000, RUR, 0 или 20000 KZT 1-3''')
  filter = {
    'salary_min':'0',
    #'salary_max':'10000000',
    'salary_currency':'RUR',
    'experience_id':'noExperience',
    'area_id':'1'
  }
  bot.send_message(message.chat.id, '''Вы ищите вакансии по запросу:
Минимальная зарплата: {}
Валюта: {}
Опыт работы: {}
Регион: Москва'''.format(filter['salary_min'],filter['salary_currency'],filter['experience_id']))
  data = util.GetDataFromServer(backend_address, backend_port, filter)
  if len(data) == 0:
    bot.send_message(message.chat.id, 'Таких вакансий не найдено!')
    return
  bot.send_message(message.chat.id, 'Для вас найдено {} вакансий!'.format(len(data)))
  for item in data:
    #bot.send_message(message.chat.id, 'Найдена вакансия:')
    bot.send_message(message.chat.id, '''Название: {}
Минимальная заработная плата: {}
Валюта: {}
Необходимый опыт работы: {}
Ссылка: {}'''.format(item['name'],item['salary_min'],item['salary_currency'],item['experience_name'],item['alternate_url']))

#------------------------------------------------------------

@bot.message_handler(commands=["refresh"])
def main(message):
  response = util.RefreshServerData(backend_address, backend_port)
  if(response['status'] == 'success'):
    bot.send_message(message.chat.id, 'Данные загружены')
  else:
    bot.send_message(message.chat.id, 'Не удалось загрузить данные')

#------------------------------------------------------------
'''
@bot.message_handler()
def text_message(message):
'''
#------------------------------------------------------------

bot.polling(non_stop=True)