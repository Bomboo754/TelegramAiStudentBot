# AI EXPLORER BOT — ENGLISH VERSION (FOR HACKATHON)
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# MY TOKEN FROM @BotFather
TOKEN = "8538943368:AAHI4EfG9crMkFmbbmdAIWMvSAp9t2-Zjww"
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Student AI Help Bot activated!\n\n"
        "Type any topic, for example:\n"
        "• space\n"
        "• dinosaurs\n"
        "• how the internet works\n\n"
        "I will ask questions and give resources — think for yourself!"
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "space" in text or "star" in text or "planet" in text or "cosmos" in text or "cosmology" in text:
        reply = (
            "Space is a mystery!\n\n"
            "Questions for you:\n"
            "1. Why doesn't the Moon fall to Earth?\n"
            "2. What would you look for on Mars?\n\n"
            "Resources:\n"
            "• https://www.youtube.com/watch?v=6PiyUjVxukI&pp=ygUJVEVEIHNwYWNl\n"
            "• https://www.khanacademy.org/science/cosmology-and-astronomyx`y"
        )
    elif "dinosaur" in text:
        reply = (
            "Dinosaurs are extinct, but the questions remain!\n\n"
            "1. Why were they so big?\n"
            "2. Could they survive today?\n\n"
            "Resources:\n"
            "• https://www.youtube.com/watch?v=PFRcEXIpBe0&pp=ygUJZGlub3NhdXJz0gcJCQMKAYcqIYzv'\n"
            "• https://kids.nationalgeographic.com/animals/prehistoric"
        )
    elif "internet" in text or "computer" in text or "web" in text or "PC" in text:
        reply = (
            "Is the Internet magic?\n\n"
            "1. How does data travel through cables?\n"
            "2. What happens if all servers shut down?\n\n"
            "Resources:\n"
            "• https://youtu.be/7_LPdttKXPc\n"
            "• Code.org"
        )
    else:
        reply = (
            f"Topic: '{update.message.text}'\n\n"
            "Great choice! Here are questions:\n"
            "1. What do you already know about this?\n"
            "2. How does it relate to your life?\n"
            "3. What would you change?\n\n"
            "Resources: search on YouTube or Khan Academy!"
        )

    await update.message.reply_text(reply)

# === BOT START (NO ERRORS ON WINDOWS + PYTHON 3.14) ===
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    print("Bot is running! Go to Telegram → /start")
    print("Press Ctrl+C to stop.")

    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()