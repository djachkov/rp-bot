def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Text sample...")
