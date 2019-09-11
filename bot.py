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
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''he is bleeding''',
    '''Is it severe?''',
    '''Yes''',
    '''Has your kid lost consciousness, is unresponsive, or is breathing irregularly?''',
    '''Yes''',
    '''Call 911, then follow these steps:

    Lay your child down with the feet elevated about 6 inches
    If possible, elevate the part of the body that's bleeding as well
    Apply firm pressure to the wound with a clean cloth until the bleeding stops
    If blood soaks through the bandage you're using, just add another layer on top
    Once the bleeding stops, leave the bandage in place and tie another bandage – or wrap plastic wrap or duct tape – firmly around the injured area (but not so tight that it could cut off circulation)
    ''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''he is bleeding''',
    '''Is it severe?''',
    '''Yes''',
    '''Has your kid lost consciousness, is unresponsive, or is breathing irregularly?''',
    '''No''',
    '''Follow these steps, call 911 if you can't stop the bleeding within ten minutes by pressing on it with a clean cloth:

    Lay your child down with the feet elevated about 6 inches
    If possible, elevate the part of the body that's bleeding as well
    Apply firm pressure to the wound with a clean cloth until the bleeding stops
    If blood soaks through the bandage you're using, just add another layer on top
    Once the bleeding stops, leave the bandage in place and tie another bandage – or wrap plastic wrap or duct tape – firmly around the injured area (but not so tight that it could cut off circulation)

    If the child is awake and alert go to the emergency room
    ''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    "Don't worry I'm here to help you, what is his emergency?",
    '''he is bleeding''',
    '''Is it severe?''',
    '''No''',
    '''Follow these steps, call 911 if you can't stop the bleeding within ten minutes by pressing on it with a clean cloth:

    Apply direct pressure with a clean bandage or towel until the bleeding stops
    Check for debris in the wound; try to flush it out with cool running water or use tweezers to carefully lift out larger debris
    Gently wash the wound well with soap and warm water or soak the wounded area in the bathtub, then pat dry
    Apply an antibiotic ointment
    Cover the wound with a bandage if it's in a spot that's likely to get dirty or rub against clothing

    Go to the emergency room if:

    The cut looks deep or has jagged edges. (Your child may need stitches.)
    The wound is embedded with debris (like dirt or gravel) that you can't get out
    The wound is on your child's face
    Your child has been bitten by an animal or another child and the skin is broken
    Your child has a deep puncture wound or cut caused by a dirty object

    Call the doctor if you see these signs of infection in the following days:

    Redness, pus, oozing, swelling, or if the area is warm to the touch
    ''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''he was poisoned''',
    '''Has your kid lost consciousness, is unresponsive, or is breathing irregularly?''',
    '''Yes''',
    '''Call 911, then follow these steps:

   Get the rest of whatever was swallowed away from your baby
    Do not try to make your baby vomit
    Try to make your baby spit out anything left in the mouth
    Keep a sample – unless you have the container
    Call Poison Control (800-222-1222), which can assess the situation and tell you what to do
    ''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''he was poisoned''',
    '''Has your kid lost consciousness, is unresponsive, or is breathing irregularly?''',
    '''No''',
    '''Is your kid having convulsions, turning blue around the mouth, or has burns on the lips or mouth?''',
    '''Yes''',
    '''Call 911, then follow these steps:

    Get the rest of whatever was swallowed away from your baby
    Do not try to make your baby vomit
    Try to make your baby spit out anything left in the mouth
    Keep a sample – unless you have the container
    Call Poison Control (800-222-1222), which can assess the situation and tell you what to do
    ''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''he was poisoned''',
    '''Has your kid lost consciousness, is unresponsive, or is breathing irregularly?''',
    '''No''',
    '''Is your kid having convulsions, turning blue around the mouth, or has burns on the lips or mouth?''',
    '''No''',
    '''That means it is not as severe, follow these steps:

    Get the rest of whatever was swallowed away from your baby
    Do not try to make your baby vomit
    Try to make your baby spit out anything left in the mouth
    Keep a sample – unless you have the container
    Call Poison Control (800-222-1222), which can assess the situation and tell you what to do
    ''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''drank a chemical''',
    '''Has your kid lost consciousness, is unresponsive, or is breathing irregularly?''',
    '''Yes''',
    '''Call 911, then follow these steps:

   Get the rest of whatever was swallowed away from your baby
    Do not try to make your baby vomit
    Try to make your baby spit out anything left in the mouth
    Keep a sample – unless you have the container
    Call Poison Control (800-222-1222), which can assess the situation and tell you what to do
    ''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''drank a chemical''',
    '''Has your kid lost consciousness, is unresponsive, or is breathing irregularly?''',
    '''No''',
    '''Is your kid having convulsions, turning blue around the mouth, or has burns on the lips or mouth?''',
    '''Yes''',
    '''Call 911, then follow these steps:

    Get the rest of whatever was swallowed away from your baby
    Do not try to make your baby vomit
    Try to make your baby spit out anything left in the mouth
    Keep a sample – unless you have the container
    Call Poison Control (800-222-1222), which can assess the situation and tell you what to do
    ''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''drank a chemical''',
    '''Has your kid lost consciousness, is unresponsive, or is breathing irregularly?''',
    '''No''',
    '''Is your kid having convulsions, turning blue around the mouth, or has burns on the lips or mouth?''',
    '''No''',
    '''That means it is not as severe, follow these steps:

    Get the rest of whatever was swallowed away from your baby
    Do not try to make your baby vomit
    Try to make your baby spit out anything left in the mouth
    Keep a sample – unless you have the container
    Call Poison Control (800-222-1222), which can assess the situation and tell you what to do
    ''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''he is vomiting''',
    '''Is your child responsive?''',
    '''no''',
    '''Call 911
    ''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''he is vomiting''',
    '''Is your child responsive?''',
    '''yes''',
    '''Does your kid present inconsolable crying, alternately pulling in and extending legs, arching back in pain?''',
    '''yes''',
    '''Go to the emergency room''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''he is vomiting''',
    '''Is your child responsive?''',
    '''yes''',
    '''Does your kid present inconsolable crying, alternately pulling in and extending legs, arching back in pain?''',
    '''no''',
    '''Does his vomit look green, black, or red?''',
    '''yes''',
    '''Go to the emergency room
    (try to bring a sample in a plastic bag)''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''he is vomiting''',
    '''Is your child responsive?''',
    '''yes''',
    '''Does your kid present inconsolable crying, alternately pulling in and extending legs, arching back in pain?''',
    '''no''',
    '''Does his vomit look green, black, or red?''',
    '''no''',
    '''Does he have a hard lump or swelling in abdomen that is painful when touched?''',
    '''yes''',
    '''Go to the emergency room''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''he is vomiting''',
    '''Is your child responsive?''',
    '''yes''',
    '''Does your kid present inconsolable crying, alternately pulling in and extending legs, arching back in pain?''',
    '''no''',
    '''Does his vomit look green, black, or red?''',
    '''no''',
    '''Does he have a hard lump or swelling in abdomen that is painful when touched?''',
    '''no''',
    '''Has your kid been vomiting more than once after a head injury?''',
    '''yes''',
    '''Go to the emergency room''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''he is vomiting''',
    '''Is your child responsive?''',
    '''yes''',
    '''Does your kid present inconsolable crying, alternately pulling in and extending legs, arching back in pain?''',
    '''no''',
    '''Does his vomit look green, black, or red?''',
    '''no''',
    '''Does he have a hard lump or swelling in abdomen that is painful when touched?''',
    '''no''',
    '''Has your kid been vomiting more than once after a head injury?''',
    '''no''',
    '''Ok, no need to panic however call the doctor if your baby has these symptoms:

    Vomiting for more than 24 hours
    Six hours without a wet diaper, dry lips and mouth, crying without tears if he's more than 3 weeks old, unusual sleepiness, dark yellow urine, sunken fontanels (the soft spots on the head)
    A little blood in the vomit
    Forceful, persistent vomiting within a half hour after eating''',
    ])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''has diarrhea''',
    '''Is he responsive?''',
    '''No''',
    '''Call 911''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''has diarrhea''',
    '''Is he responsive?''',
    '''Yes''',
    '''Don't worry no need to call 911, however call the doctor if your baby has these symptoms:

    Baby younger than 3 months has diarrhea (stools that are suddenly more frequent and more watery than usual)
    Diarrhea not improving after 24 hours
    Six hours without a wet diaper, dry lips and mouth, crying without tears if he's more than 3 weeks old, unusual sleepiness, dark yellow urine, sunken fontanels (the soft spots on the head)
    Black stool or blood in the stool''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''broke bone''',
    '''Is the bone is sticking out of the skin.?''',
    '''Yes''',
    '''Call 911
    (Don't touch the bone. Cover it with a clean cloth.)''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''broke bone''',
    '''Is the bone is sticking out of the skin.?''',
    '''no''',
    '''May your child have a skull, neck, back, or pelvic fracture. '''
    '''yes''',
    '''Call 911 and don't move your child.''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''broke bone''',
    '''Is the bone is sticking out of the skin.?''',
    '''no''',
    '''May your child have a skull, neck, back, or pelvic fracture. '''
    '''no''',
    '''Ok no need to worry, however call the doctor if your baby has these signs of a broken bone:

    Bruising, swelling, tenderness, and stiffness in one area
    Increased pain with movement
    Unwillingness to use limb
    Limb seems bent out of position
    You heard a snapping sound during trauma'''
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''hit head fell down''',
    '''Is your child presenting irregular breathing, convulsions or seizure, or unconsciousness?''',
    '''yes''',
    '''Call 911
     In the meantime:

    Don't move your baby unless there's danger of being hurt further
    Perform CPR if baby stops breathing
    If baby is bleeding, cover the wound with a clean cloth and apply pressure'''
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''hit head fell down''',
    '''Is your child presenting irregular breathing, convulsions or seizure, or unconsciousness?''',
    '''no''',
    '''Ok, go to the emergency room or call a doctor right away if:
    Child was unconscious, even if child seems fine afterward
    Child vomits more than once
    Child is unusually sleepy
    Child seems weak or confused or has problems with coordination, vision, or verbal communication
    Child is bleeding from the ears
    Child has bleeding from the nose or mouth that doesn't stop after five to ten minutes of applying pressure (see "what to do" above)'''
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''seizure''',
    '''Turn your child on the side to prevent choking on saliva, and wipe saliva away from the mouth to keep the airway clear.
    Did the seizure last longer than 3 minutes?''',
    '''no''',
    '''Is your child turning blue around the mouth or taking more than 60 breaths per minute''',
    '''no''',
    '''Can you reach the doctor right away?''',
    '''yes''',
    '''Call a doctor''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''seizure''',
    '''Turn your child on the side to prevent choking on saliva, and wipe saliva away from the mouth to keep the airway clear.
    Did the seizure last longer than 3 minutes?''',
    '''no''',
    '''Is your child turning blue around the mouth or taking more than 60 breaths per minute''',
    '''no''',
    '''Can you reach the doctor right away?''',
    '''no''',
    '''Call 911''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''seizure''',
    '''Turn your child on the side to prevent choking on saliva, and wipe saliva away from the mouth to keep the airway clear.
    Did the seizure last longer than 3 minutes?''',
    '''no''',
    '''Is your child turning blue around the mouth or taking more than 60 breaths per minute''',
    '''yes''',
    '''Call 911''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''seizure''',
    '''Turn your child on the side to prevent choking on saliva, and wipe saliva away from the mouth to keep the airway clear.
    Did the seizure last longer than 3 minutes?''',
    '''yes''',
    '''Call 911''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''trouble breathing''',
    '''Is your child turning blue around the mouth or taking more than 60 breaths per minute?''',
    '''yes''',
    '''Call 911''',
])
trainer.train([
    "Is your child breathing?",
    '''yes''',
    '''Don't worry I'm here to help you, what is his emergency?''',
    '''trouble breathing''',
    '''Is your child turning blue around the mouth or taking more than 60 breaths per minute?''',
    '''no''',
    '''Ok, however call your doctor if your child presents any of the symptoms:
    Grunting
    Flaring nostrils
    Sucking in the skin above the collarbone, or between or below the ribs
    Consistently fast breathing
    Whistling, coughing, or crackly sounds on inhale and exhale (wheezing)
    ''',
])
trainer.train([
    "Is your child breathing?",
    '''no''',
    '''Is your child less than 1 year old?''',
    '''yes'''
    '''Ask a bystander to call 911 and retrieve an AED. If there is no bystander, call 911 after delivering 2 minutes of care.
    Open the airway. With the child lying on his or her back, tilt the head back slightly and lift the chin.
    Deliver 2 rescue breaths if the child or infant isn't breathing. With the head tilted back slightly and the chin lifted, use your mouth to make a complete seal over the infant's mouth and nose, then blow in for one second to make the chest clearly rise. Now, deliver two rescue breaths.
    Perform CPR:

    Kneel beside the child or baby.

    Push hard, push fast. Use 2 fingers to deliver 30 quick compressions that are each about 1.5 inches deep.

    Give 2 rescue breaths (see instructions above).

    Keep going. Continue the these baby or child CPR steps until you see obvious signs of life, like breathing, or until an AED is ready to use, another trained responder or EMS professional is available to take over, you're too exhausted to continue, or the scene becomes unsafe.
    ''',
    
])
trainer.train([
    "Is your child breathing?",
    '''no''',
    '''Is your child less than 1 year old?''',
    '''no'''
    '''Ask a bystander to call 911 and retrieve an AED. If there is no bystander, call 911 after delivering 2 minutes of care.
    Open the airway. With the child lying on his or her back, tilt the head back slightly and lift the chin.
    Deliver 2 rescue breaths if the child or infant isn't breathing. With the head tilted back slightly and the chin lifted, pinch the child's nose shut, make a complete seal by placing your mouth over the child's mouth and breathe into the child's mouth twice.
    Perform CPR:

    Kneel beside the child or baby.

    Push hard, push fast. place the heel of one hand on the center of the chest, then place the heel of the other hand on top of the first hand, and lace your fingers together. Deliver 30 quick compressions that are each about 2 inches deep.

    Give 2 rescue breaths (see instructions above).

    Keep going. Continue the these baby or child CPR steps until you see obvious signs of life, like breathing, or until an AED is ready to use, another trained responder or EMS professional is available to take over, you're too exhausted to continue, or the scene becomes unsafe.
    ''',
    
])

