from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot(
    "Zeroni",
    logic_adapter=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)
trainer = ListTrainer(bot)

trainer.train([
    "My baby is choking.",
    "Call your doctor."
])

print("Hi! What's wrong? ")

while True:
    try:
        bot_input = bot.get_response(input("> "))
        print(bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
