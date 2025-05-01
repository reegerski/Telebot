
import os
from telegram.ext import Updater, CommandHandler

# Get token from Render environment variable
TOKEN = os.getenv('BOT_TOKEN')

# Command: /start
def start(update, context):
    update.message.reply_text("Welcome to Digital Profit Mob! Type /help to see everything I can do.")

# Command: /picks
def picks(update, context):
    update.message.reply_text("Today’s free sports betting picks:\n\n- [Insert picks here]")

# Command: /record
def record(update, context):
    update.message.reply_text("Recent Win/Loss Record:\n\nWeek: 12-4\nMonth: 42-21")

# Command: /vip
def vip(update, context):
    update.message.reply_text("To join the VIP group, visit:\nhttps://yourviplink.com\nOr DM @yourhandle for access.")

# Command: /units
def units(update, context):
    update.message.reply_text("Unit sizing tips:\n\n- 1 unit = 2% of bankroll\n- Increase unit size every 35u profit\n- Never chase losses!")

# Command: /rules
def rules(update, context):
    update.message.reply_text("Group Rules:\n\n1. Respect all members\n2. No spam or self-promo\n3. Stick to unit system\n4. Trust the process")

# Command: /help
def help_command(update, context):
    update.message.reply_text("""Available Commands:
/picks – Get today’s free sports betting picks
/record – View recent win/loss record
/vip – How to join the VIP group
/units – Learn about unit sizing and bankroll tips
/rules – Group rules & betting guidelines
/socials – Links to all DPM platforms
/about – Info about Digital Profit Mob
/support – Contact for help or issues""")

# Command: /socials
def socials(update, context):
    update.message.reply_text("DPM Socials:\nInstagram: https://instagram.com/dpm\nTwitter: https://twitter.com/dpm\nTikTok: https://tiktok.com/@dpm")

# Command: /about
def about(update, context):
    update.message.reply_text("Digital Profit Mob is a premium betting community that helps you flip your bankroll with discipline, smart plays, and group support.")

# Command: /support
def support(update, context):
    update.message.reply_text("For help or support, DM @yourhandle or email support@dpm.com")

# Set up bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register all command handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('picks', picks))
dispatcher.add_handler(CommandHandler('record', record))
dispatcher.add_handler(CommandHandler('vip', vip))
dispatcher.add_handler(CommandHandler('units', units))
dispatcher.add_handler(CommandHandler('rules', rules))
dispatcher.add_handler(CommandHandler('help', help_command))
dispatcher.add_handler(CommandHandler('socials', socials))
dispatcher.add_handler(CommandHandler('about', about))
dispatcher.add_handler(CommandHandler('support', support))

# Start polling
updater.start_polling()
updater.idle()
