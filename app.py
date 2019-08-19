# coding: utf8
import logging
import random

from Character import Character
from config import token
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler
from telegram.ext import Updater

"""
 ____
|    |
|____|
"""
characters = {}
en_does_not_exist = "{} does not exist!"
ru_does_not_exist = "{} не существует."
HELP = """Привет, {}!
Краткое описание существующих комманд:
/start - начать диалог с ботом
/help - получить список комманд
/character - создание персонажа
/attack <username> атаковать персонажа
/levelup - повысить свой уровень
/improve <ability> - потратить очко навыков на характеристики
Список характеристик (с начальным значением):
strength=5,
dexterity=5,
constitution=5,
intelligence=5,
wisdom=5,
charisma=5

"""

def help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=HELP.format(update.message.from_user.username))

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=START_MESSAGE)

def create_character(update, context):
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    character_id = '/'.join([str(chat_id), str(user_id)])
    name = update.message.from_user.username
    if name not in characters:
        characters[name] = Character(character_id, name)
        context.bot.send_message(chat_id=chat_id, text=f"{name} was created")
    else:
        context.bot.send_message(chat_id=chat_id, text=f"{name} already exist!")

def attack(update, context):
    chat_id = update.message.chat_id
    name = update.message.from_user.username
    user_message = update.message.text.split(' ')
    if len(user_message) < 2:
        update.message.reply_text("I'm sorry Dave I'm afraid I can't do that.")
    else:
        enemy_name = user_message[1]
    if name in characters and enemy_name in characters:
        damage = characters[name].physical_damage
        armour = characters[enemy_name].armour
        health = characters[enemy_name].health
        context.bot.send_message(chat_id=chat_id,
                                 text=f"{name} атакует {enemy_name} и наносит {damage} урона!\n"
                                 f"У {enemy_name} осталось {armour} брони и {health} здоровья!")
        characters[enemy_name].get_damage(damage)
        if characters[enemy_name].health <= 0:
            context.bot.send_message(chat_id=chat_id,
                                     text=f"{enemy_name} бесславно погиб в бою")
            del characters[enemy_name]
    elif name not in characters:
        context.bot.send_message(chat_id=chat_id,
                                 text=f"{name} не создан")
    elif enemy_name not in characters:
        context.bot.send_message(chat_id=chat_id,
                                 text=f"{enemy_name} не создан")
def equip(update, context):
    chat_id = update.message.chat_id
    name = update.message.from_user.username
    user_message = update.message.text.split(' ')
    weapon = user_message[1]
    char = characters[name]

    context.bot.send_message(chat_id=chat_id,
                             text=char.equip(weapon))
def improve(update, context):
    chat_id = update.message.chat_id
    name = update.message.from_user.username
    ability = update.message.text[9::]
    try:
        char = characters[name]
        char.improve_ability(ability)
        skill_points = char.skill_points
        context.bot.send_message(chat_id=chat_id,
                                 text=f"{name} повысил свою {ability}\nYou have {skill_points} left")
    except KeyError:
        context.bot.send_message(chat_id=chat_id,
                                 text=ru_does_not_exist.format(name))

def level_up(update, context):
    chat_id = update.message.chat_id
    name = update.message.from_user.username
    try:
        char = characters[name]
        char.levelup()
        skill_points = char.skill_points
        context.bot.send_message(chat_id=chat_id,
                                 text=f"{name} level up!\nYou have {skill_points} skillpoints to improve your abilities!")
    except KeyError:
        context.bot.send_message(chat_id=chat_id,
                                 text=ru_does_not_exist.format(name))


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


def luck(update, context):
    # d4 = random.randrange(1, 4)
    # d6 = random.randrange(1, 6)
    # d8 = random.randrange(1, 8)
    # d10 = random.randrange(1, 10)
    # d12 = random.randrange(1, 12)
    # d20 = random.randrange(1, 20)
    # d30 = random.randrange(1, 30)
    d100 = random.randrange(1, 100)
    context.bot.send_message(chat_id=update.message.chat_id, text=str(d100))


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    if query == "random":
        results = list()
        results.append(
            InlineQueryResultArticle(
                id=str(random.randrange(1, 100)),
                title='Random',
                input_message_content=InputTextMessageContent("The dice said: " + str(random.randrange(1, 12)))
            )
        )
        context.bot.answer_inline_query(update.inline_query.id, results)

def monitor(update, context):
    chat_id = update.message.chat_id
    name = update.message.from_user.username
    context.bot.send_message(chat_id=chat_id, text=f"{characters[name].__dict__}")
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    enSTART_MESSAGE = "Welcome, stranger! Do you ready for an alpha-test adventure? \n Use /character command to create a new and shiny character for you!"
    START_MESSAGE = "Добро пожаловать, незнакомец! Готовы ли вы к альфа-тесту приключений? \ n Используйте команду / character, чтобы создать для вас нового и блестящего персонажа!"
    start_handler = CommandHandler('start', start)
    luck = CommandHandler('luck', luck)
    levelup = CommandHandler('levelup', level_up)
    new_character = CommandHandler('character', create_character)
    attack = CommandHandler('attack', attack)
    improve = CommandHandler('improve', improve)
    help = CommandHandler('help', help)
    equip = CommandHandler('equip', equip)
    monitor = CommandHandler('monitor', monitor)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(luck)
    dispatcher.add_handler(new_character)
    dispatcher.add_handler(levelup)
    dispatcher.add_handler(attack)
    dispatcher.add_handler(improve)
    dispatcher.add_handler(help)
    dispatcher.add_handler(equip)
    dispatcher.add_handler(monitor)
    inline_caps_handler = InlineQueryHandler(inline_caps)

    updater.start_polling()
    updater.idle()