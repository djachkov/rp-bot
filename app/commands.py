# TODO: add basic commands
def start(update, context):
    chid = update.effective_chat.id
    context.bot.send_message(chat_id=chid, text=chid)
