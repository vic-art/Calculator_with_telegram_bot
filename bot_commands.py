from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler,
                          ContextTypes, ConversationHandler,
                          MessageHandler, filters)
from controller import run as compute

(ADD_FIRST_NUMBER, ADD_SECOND_NUMBER, ADD_OPERATION) = range(3)


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Вас приветствует калькулятор.\n"
                                    "Пожалуйста, введите первое число:")
    return ADD_FIRST_NUMBER


async def parse_first_num(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    num_1 = update.message.text
    context.user_data['number_1'] = num_1
    await update.message.reply_text("Введите второе число:")
    return ADD_SECOND_NUMBER


async def parse_second_num(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    num_2 = update.message.text
    context.user_data['number_2'] = num_2
    await update.message.reply_text("Введите операцию (+-*/):")
    return ADD_OPERATION


async def parse_operation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    op = update.message.text
    a = context.user_data['number_1']
    b = context.user_data['number_2']
    res = compute(a, b, op)
    await update.message.reply_text(res)
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    app = ApplicationBuilder().token(
        "here_should_be_token").build()

    # Add conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", welcome)],
        allow_reentry=True,
        states={  # список возможных состояний диалога с ботом
            # обработчики события получения сообщения от пользователя
            ADD_FIRST_NUMBER: [MessageHandler(filters.ALL, parse_first_num)],
            ADD_SECOND_NUMBER: [MessageHandler(filters.ALL, parse_second_num)],
            ADD_OPERATION: [MessageHandler(filters.ALL, parse_operation)]
        },
        fallbacks=[welcome]
    )

    app.add_handler(conv_handler)

    app.run_polling()


if __name__ == "__main__":
    main()
