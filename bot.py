import random
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes

def utku1(bin_taban):
    rakamlar = [int(r) for r in bin_taban]
    for i in range(len(rakamlar) - 1, -1, -2):
        rakamlar[i] *= 2
        if rakamlar[i] > 9:
            rakamlar[i] -= 9
    return (sum(rakamlar) * 9) % 10

def utku2(bin_numarasi):
    kart_numarasi = bin_numarasi + ''.join(str(random.randint(0, 9)) for _ in range(15 - len(bin_numarasi)))
    kontrol_rakami = utku1(kart_numarasi)
    kart_numarasi += str(kontrol_rakami)
    ay = str(random.randint(1, 12)).zfill(2)
    yil = str(random.randint(2025, 2030))
    cvv = str(random.randint(100, 999)).zfill(3)
    return f"{kart_numarasi}|{ay}|{yil}|{cvv}"

async def gen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        bin_numarasi = context.args[0]
        if not bin_numarasi.isdigit() or len(bin_numarasi) != 6:
            await update.message.reply_text("❌ সঠিক ৬-অঙ্কের BIN নম্বর দিন")
            return
        sonuc = [utku2(bin_numarasi) for _ in range(10)]
        await update.message.reply_text("\n".join(sonuc))
    except IndexError:
        await update.message.reply_text("⚡ ব্যবহার: /gen <BIN>  (১০টা কার্ড আসবে)")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Bot Started!\nব্যবহার: /gen <BIN>\n\nℹ️ সব কমান্ড দেখতে /help লিখুন"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "📌 Bot কমান্ডসমূহ:\n\n"
        "/start - Bot শুরু করুন\n"
        "/gen <BIN> - ১০টা কার্ড জেনারেট হবে\n"
        "/help - সাহায্য মেনু"
    )
    await update.message.reply_text(msg)

async def post_init(app: Application):
    await app.bot.set_my_commands([
        BotCommand("start", "বট চালু করুন"),
        BotCommand("gen", "১০টা কার্ড জেনারেট হবে"),
        BotCommand("help", "সাহায্য মেনু")
    ])

if __name__ == "__main__":
    TOKEN = "8361609703:AAH2iwaDiSNTdQVpPBvSpQt0KWTX8qpGlmE"  # এখানে আপনার বট টোকেন বসান
    app = Application.builder().token(TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gen", gen))
    app.add_handler(CommandHandler("help", help_cmd))
    print("Bot is running...")
    app.run_polling()
