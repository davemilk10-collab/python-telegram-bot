from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

CHANNEL_ID = "@dragonstrending"

def vote(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    chat_member = context.bot.get_chat_member(CHANNEL_ID, user_id)

    if chat_member.status in ["member", "administrator", "creator"]:
        project = " ".join(context.args)
        if project:
            update.message.reply_text(f"✅ Your vote for {project} has been recorded!")
            # save vote in DB or Google Sheet here
        else:
            update.message.reply_text("⚠️ Please specify a project name. Example: /vote Gashy")
    else:
        update.message.reply_text("❌ You must join our channel first: https://t.me/YourChannel")

updater = Updater("8323882698:AAG09u4nIL1ychjc1lk5H9bp8dEsKppA9UM")
dp = updater.dispatcher
dp.add_handler(CommandHandler("vote", vote))

updater.start_polling()
updater.idle()

