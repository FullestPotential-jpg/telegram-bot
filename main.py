from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ЗАМЕНИ НА СВОЙ ТОКЕН от BotFather!
BOT_TOKEN = "8420860789:AAETOuPb4hbTe5aK-AXdJi-7uwo1rKLBEAw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    payment_info = """
• Платформа по реализации вашего потенциала (3 Модуля — 10 Подмодулей)

💳 *Информация об оплате:*

💰 Сумма: 395 рублей ($5)
📞 После оплаты пришлите скриншот чека сюда: @Dimasurkov1 - Выдадим вам доступ

Нажмите кнопку "Оплатить" чтобы получить реквизиты
    """
    
    keyboard = [[InlineKeyboardButton("💳 Оплатить", callback_data="get_payment_details")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        payment_info,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "get_payment_details":
        payment_details = """
✅ *Реквизиты для оплаты*
Оплата через Юмани

📱 **Номер Юмани:** `4100 1188 0154 2691`
💰 **Сумма:** 395 рублей ($5)

📋 *Инструкция:*
1. Перейдите в Юмани
3. Введите номер кошелька и сумму
3. Оплатите
4. Пришлите скриншот чека сюда: @Dimasurkov1 - Выдадим вам доступ
        """
        
        await query.message.reply_text(
            payment_details,
            parse_mode='Markdown'
        )

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.run_polling()

if __name__ == "__main__":
    main()
