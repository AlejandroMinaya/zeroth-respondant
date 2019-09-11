from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
Zeroni = ChatBot(
    "Zeroni",
    logic_adapter=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)
trainer = ListTrainer(Zeroni)
trainer.train([
    'yes',
    "Don't worry I'm here to help you, what is his emergency?",
    'he is bleeding',
    'Is it severe?',
    'Yes',
    'Has your kid lost consciousness, is unresponsive, or is breathing irregularly?',
    'Yes',
    '''Call 911, then follow these steps:

    Lay your child down with the feet elevated about 6 inches
    If possible, elevate the part of the body that's bleeding as well
    Apply firm pressure to the wound with a clean cloth until the bleeding stops
    If blood soaks through the bandage you're using, just add another layer on top
    Once the bleeding stops, leave the bandage in place and tie another bandage – or wrap plastic wrap or duct tape – firmly around the injured area (but not so tight that it could cut off circulation)
    ''',
])
