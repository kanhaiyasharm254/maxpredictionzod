import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

# 📄 Logging Setup
logging.basicConfig(
    filename='logs/bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 🔁 Your Prediction Pattern
prediction_pattern = ['🟢 GREEN', '🔴 RED', '🟣 VIOLET']
current_index = 0

# 🤖 Your Bot Token
BOT_TOKEN = "7467409659:AAECM2gp_2LQfgDYVO9fh5NKCJkucUBXAzk"

# 👋 Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to MaxPredictionZod!")
    logging.info(f"/start used by {update.effective_user.id}")

# 🎯 Predict Command
async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_index
    prediction = prediction_pattern[current_index]
    current_index = (current_index + 1) % len(prediction_pattern)

    await update.message.reply_text(f"🧠 Prediction: {prediction}")
    logging.info(f"Prediction sent to user {update.effective_user.id}: {prediction}")

# 🛠️ Main App Runner
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))

    logging.info("Bot started.")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
