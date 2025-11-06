# AI EXPLORER BOT — SIMPLE VERSION (FOR HACKATHON)
# ----------------------------------------------------
# WHAT DOES THE BOT DO?
# 1. Student types a topic (e.g. "space")
# 2. Bot asks 2–3 open-ended questions
# 3. Gives 1–2 useful resources (YouTube, Khan Academy)
# 4. NEVER gives direct answers — makes you think!
# ----------------------------------------------------
# HOW TO RUN?
# 1. Run: python bot.py
# 2. In Telegram: /start → type topic → explore!
# ----------------------------------------------------

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# REPLACE WITH YOUR REAL TOKEN FROM @BotFather
TOKEN = "8538943368:AAHI4EfG9crMkFmbbmdAIWMvSAp9t2-Zjww"
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! I'm Student AI Help Bot Prototype made by team 'BrainStormers!'\n\n"
        "My goal — help you explore the world on your own.\n\n"
        "How it works:\n"
        "1. Type any topic (e.g. space, dinosaurs, internet)\n"
        "2. I ask questions to make you think\n"
        "3. I give links to resources — figure it out yourself!\n\n"
        "Try it: type 'space'"
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()

    # ——— SPACE ———
    if any(word in text for word in ["space", "cosmos", "star", "planet", "moon", "mars"]):
        reply = (
            "Space is a mystery!\n\n"
            "Questions to think about:\n"
            "1. Why are planets round?\n"
            "2. What would you look for on Mars?\n\n"
            "Resources:\n"
            "• https://www.youtube.com/watch?v=6PiyUjVxukI&pp=ygUJVEVEIHNwYWNl\n"
            "• https://www.khanacademy.org/science/cosmology-and-astronomyx`"
        )

    # ——— DINOSAURS ———
    elif any(word in text for word in ["dinosaur", "tyrannosaurus", "extinct"]):
        reply = (
            "Dinosaurs — a puzzle from the past!\n\n"
            "Questions:\n"
            "1. Why were they so big?\n"
            "2. Could they survive today?\n\n"
            "Resources:\n"
            "• https://www.youtube.com/watch?v=PFRcEXIpBe0&pp=ygUJZGlub3NhdXJz0gcJCQMKAYcqIYzv'\n"
            "• https://kids.nationalgeographic.com/animals/prehistoric"
        )

    # ——— INTERNET ———
    elif any(word in text for word in ["internet", "computer", "web", "data"]):
        reply = (
            "Is the Internet magic?\n\n"
            "Questions:\n"
            "1. How does data travel through cables?\n"
            "2. What happens if all servers shut down?\n\n"
            "Resources:\n"
            "• https://youtu.be/7_LPdttKXPc\n"
            "• https://code.org"
        )

    # ——— DEFAULT (any topic) ———
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

# === BOT START ===
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    print("Bot is running! Go to Telegram → /start")
    print("Press Ctrl+C to stop.")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()