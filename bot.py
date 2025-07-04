from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

# 👇 Your prediction pattern
prediction_pattern = ['🟢 GREEN', '🔴 RED', '🟡 VIOLET']
current_index = 0

# Token from @BotFather
BOT_TOKEN = '7467409659:AAECM2gp_2LQfgDYVO9fh5NKCJkucUBXAzk'

# Welcome Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Welcome to Max Prediction ZOD Bot!\nNext prediction: Use /predict\nTringa 91 Club | DM Win | Abhi App")

# Predict Command
async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_index
    prediction = prediction_pattern[current_index]
    current_index = (current_index + 1) % len(prediction_pattern)
    await update.message.reply_text(f"📊 Prediction: {prediction}")

# Auto-predict every 1 min
async def auto_predict(context: ContextTypes.DEFAULT_TYPE):
    global current_index
    prediction = prediction_pattern[current_index]
    current_index = (current_index + 1) % len(prediction_pattern)
    chat_id = context.job.chat_id
    await context.bot.send_message(chat_id=chat_id, text=f"🔄 Auto Prediction: {prediction}")

async def auto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Auto predictions started every 60 seconds.")
    context.job_queue.run_repeating(auto_predict, interval=60, first=0, chat_id=update.effective_chat.id)

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.job_queue.stop()
    await update.message.reply_text("⛔ Auto predictions stopped.")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("predict", predict))
app.add_handler(CommandHandler("auto", auto))
app.add_handler(CommandHandler("stop", stop))

app.run_polling()
