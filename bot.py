from telegram import Update, ChatPermissions
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import datetime

YOUR_USER_ID = 5377960160  # Ваш ID
BOT_TOKEN = "6818744033:AAEm61z_vOldqTUyfZ8k3rK1MhV0kZRCSL8"  # Токен вашего бота

# Обработка команды "rek"
async def handle_rek(update: Update, context):
    if update.message.reply_to_message and 'rek' in update.message.text.lower() and update.message.from_user.id == YOUR_USER_ID:
        mute_time = datetime.timedelta(days=5)
        await context.bot.restrict_chat_member(
            chat_id=update.message.chat_id,
            user_id=update.message.reply_to_message.from_user.id,
            permissions=ChatPermissions(can_send_messages=False),
            until_date=datetime.datetime.now() + mute_time
        )
        # Удаление сообщения
        await context.bot.delete_message(
            chat_id=update.message.chat_id,
            message_id=update.message.reply_to_message.message_id
        )
        await context.bot.send_message(
            chat_id=update.message.chat_id, 
            text=f"Zамутил лаха на {mute_time}!"
        )

# Обработка команды "18p"
async def handle_18p(update: Update, context):
    if update.message.reply_to_message and '18p' in update.message.text.lower() and update.message.from_user.id == YOUR_USER_ID:
        mute_time = datetime.timedelta(hours=5)
        await context.bot.restrict_chat_member(
            chat_id=update.message.chat_id,
            user_id=update.message.reply_to_message.from_user.id,
            permissions=ChatPermissions(can_send_messages=False),
            until_date=datetime.datetime.now() + mute_time
        )
        # Удаление сообщения
        await context.bot.delete_message(
            chat_id=update.message.chat_id,
            message_id=update.message.reply_to_message.message_id
        )
        await context.bot.send_message(
            chat_id=update.message.chat_id, 
            text=f"Zамутил лаха на {mute_time}!"
        )

# Обработка команды "rod"
async def handle_rod(update: Update, context):
    if update.message.reply_to_message and 'rod' in update.message.text.lower() and update.message.from_user.id == YOUR_USER_ID:
        mute_time = datetime.timedelta(days=1)
        await context.bot.restrict_chat_member(
            chat_id=update.message.chat_id,
            user_id=update.message.reply_to_message.from_user.id,
            permissions=ChatPermissions(can_send_messages=False),
            until_date=datetime.datetime.now() + mute_time
        )
        # Удаление сообщения
        await context.bot.delete_message(
            chat_id=update.message.chat_id,
            message_id=update.message.reply_to_message.message_id
        )
        await context.bot.send_message(
            chat_id=update.message.chat_id, 
            text=f"Zамутил лаха на {mute_time}!"
        )

# Обработка команды "list" (вывод команд и времени мута)
async def handle_list(update: Update, context):
    if update.message.from_user.id == YOUR_USER_ID and update.message.text.lower() == "list":
        commands = """
        Список команд:
        rek - замутить на 5 дней
        18p - замутить на 5 часов
        rod - замутить на 1 день
        """
        await context.bot.send_message(
            chat_id=update.message.chat_id, 
            text=commands
        )

# Обработчик ошибок
async def error_handler(update: Update, context):
    print(f"Произошла ошибка: {context.error}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Команды для обработки
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('rek'), handle_rek))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('18p'), handle_18p))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('rod'), handle_rod))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('list'), handle_list))  # Команда list без "/"

    # Обработчик ошибок
    application.add_error_handler(error_handler)

    print("Бот запущен!")
    application.run_polling()