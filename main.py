
import telebot as tb
from telebot import types
from products import menu, product, product2, costs

# out telegram token
token = "5795865228:AAHkduJaqdL5tHuzfl9Uux7KqTY3r-8Bp_g"
bot = tb.TeleBot(token)

# saves clients' offers
offer = {}

# start page for greeting
@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(
        message.chat.id,
        f'Hi, {message.from_user.first_name}, с вами <i>Boost Energy</i>',
        parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Меню")
    item2 = types.KeyboardButton("Заказ")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,
                     'Выберите что вам надо',
                     reply_markup=markup)

# main function
@bot.message_handler(content_types=['text'])
def reply1(message):
    if message.text == 'Меню': #shows menu
        bot.send_message(message.chat.id, menu)
    else: #any other message will lead to offer
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Напитки (газ)")
        item2 = types.KeyboardButton("Энергетики")
        item3 = types.KeyboardButton("Чипсы")
        item4 = types.KeyboardButton("Напитки (без газ)")
        markup.add(item1, item2, item3, item4)
        msg = bot.send_message(message.chat.id, 'Choose', reply_markup=markup)
        bot.register_next_step_handler(msg, reply2) # calling next function to check what's choosen


def reply2(message):

    if message.text == "Напитки (газ)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Cola")
        item2 = types.KeyboardButton("Fanta")
        item3 = types.KeyboardButton("Sprite")
        item4 = types.KeyboardButton("Pepsi")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4, item5)

    elif message.text == "Энергетики":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Gorilla")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item5)

    elif message.text == "Чипсы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Lays")
        item3 = types.KeyboardButton("Grizzly")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item3, item5)

    elif message.text == "Напитки (без газ)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Piko")
        item2 = types.KeyboardButton("Fuse tea")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item5)
    else:
        bot.send_message(message.chat.id, 'Я не понимаю вас. Попробуйте еще')
        reply1(message)

    msg = bot.send_message(message.chat.id,
                               'Какой вкус: ',
                               reply_markup=markup)
    bot.register_next_step_handler(msg, reply2_taste)


def reply2_taste(message):
    if message.text == "Fuse tea":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Манго ананас")
        item2 = types.KeyboardButton("Лимон")
        item3 = types.KeyboardButton("Ягода")
        item4 = types.KeyboardButton("Персик")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4, item5)
        msg = bot.send_message(message.chat.id,
                               'Какой вкус: ',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, reply3)

    elif message.text == "Piko":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Морс")
        item2 = types.KeyboardButton("Апельсин")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item5)
        msg = bot.send_message(message.chat.id,
                               'Какой вкус: ',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, reply3)

    elif message.text == "Lays":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Сыр")
        item2 = types.KeyboardButton("Шашлык")
        item3 = types.KeyboardButton("Паприка")
        item4 = types.KeyboardButton("Крылышки")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4, item5)
        msg = bot.send_message(message.chat.id,
                               'Какой вкус: ',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, reply3)

    elif message.text == "Gorilla":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Original")
        item2 = types.KeyboardButton("Mango")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item5)
        msg = bot.send_message(message.chat.id,
                               'Какой вкус: ',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, reply3)

    else:
        reply3(message) # some products do not need to choose taste that is why we call for them next function


def reply3(message):
    if message.text == 'Назад': # sends to home page
        reply1(message)
    else:
        key = product2[message.text] # gets unique key id of offer
        val = product[key] # checks how much left 
        
        bot.send_message(message.chat.id, f'В наличий {val} штук')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("1")
        item2 = types.KeyboardButton("2")
        item3 = types.KeyboardButton("3")
        item4 = types.KeyboardButton("4")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4, item5)
        offer['type'] = message.text # offer saves offer's type eg 'COla'
        offer['key'] = key # that's unique id eg '1000'
        msg = bot.send_message(message.chat.id,
                            'Сколько штук ',
                            reply_markup=markup)
        bot.register_next_step_handler(msg, reply3_val_check)

def reply3_val_check(msg):
    if msg.text == 'Назад':
        reply1(msg)
    elif int(msg.text) > int(product[offer['key']]): # checks if client wants more than store have it reask the number of offer
        bot.send_message(msg.chat.id, 'Ошибка, Повторите заказ(((')
        reply3(offer['type'])
    else:
        offer['count'] = msg.text
        reply3_block1(msg) # next function


def reply3_block1(message):
    # here we get info about clietns' block
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True )
    item1 = types.KeyboardButton("22")
    item2 = types.KeyboardButton("23")
    item3 = types.KeyboardButton("24")
    item4 = types.KeyboardButton("25")
    item5 = types.KeyboardButton("26")
    item6 = types.KeyboardButton("27")
    markup.add(item1, item2, item3, item4, item5, item6)
    msg = bot.send_message(message.chat.id,
                            'Block:',
                            reply_markup=markup)
    bot.register_next_step_handler(msg, reply3_block2)
def reply3_block2(message):
    # here we get info about room
    offer['block'] = message.text
    msg = bot.send_message(message.chat.id,
                            'Room:')
    bot.register_next_step_handler(msg, reply3_room)

def reply3_room(message):
    # it asks is the offer correct
    offer['room'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton("Подтвердить")
    item2 = types.KeyboardButton("Сначала")
    markup.add(item1, item2)
    num = offer['count']
    tipe = offer['type']
    block = offer['block']
    room = offer['room']
    cost = costs[offer['key']]
    msg = bot.send_message(message.chat.id,
                            f'Вы заказали {num} шт {tipe} в {block} {room}.\nК оплате {str(int(cost) * int(num))} тг',
                            reply_markup=markup)
    bot.register_next_step_handler(msg, confirm)

def confirm(message):
    # confirms that offer data is correct and sends offer details to direct of seller
    if message.text == 'Подтвердить':
        num = offer['count']
        tipe = offer['type']
        block = offer['block']
        room = offer['room']
        cost = costs[offer['key']]
        product[offer['key']] = str(int(product[offer['key']]) - int(num))
        bot.send_message(message.chat.id,
                                'Ваш заказ будет доставлен через 15 мин')
        bot.send_message(967604546,
                                    f'Заказ {num} шт {tipe} в {block} {room}.\nК оплате {str(int(cost) * int(num))} тг')
        reply1(message)
        
    else:
        reply1(message)


bot.polling(none_stop=True)
