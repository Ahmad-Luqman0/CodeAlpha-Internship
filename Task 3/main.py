import spacy
from spacy.matcher import Matcher
import random


nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)


patterns = [
    {"label": "GREET", "pattern": [{"LOWER": "hello"}]},
    {"label": "GREET", "pattern": [{"LOWER": "hi"}]},
    {"label": "GREET", "pattern": [{"LOWER": "hey"}]},
    {"label": "GREET", "pattern": [{"LOWER": "good"}, {"LOWER": "morning"}]},
    {"label": "GREET", "pattern": [{"LOWER": "good"}, {"LOWER": "evening"}]},
    {"label": "GREETINGS", "pattern": [{"LOWER": "how"}, {"LOWER": "are"}, {"LOWER": "you"}]},
    {"label": "BYE", "pattern": [{"LOWER": "allah"}, {"LOWER": "hafiz"}]},
    {"label": "BYE", "pattern": [{"LOWER": "bye"}]},
    {"label": "BYE", "pattern": [{"LOWER": "goodbye"}]},
    {"label": "BYE", "pattern": [{"LOWER": "see"}, {"LOWER": "you"}, {"LOWER": "later"}]},
    {"label": "THANKS", "pattern": [{"LOWER": "thank"}, {"LOWER": "you"}]},
    {"label": "THANKS", "pattern": [{"LOWER": "thanks"}]},
    {"label": "NAME", "pattern": [{"LOWER": "what"}, {"LOWER": "is"}, {"LOWER": "your"}, {"LOWER": "name"}]},
    {"label": "NAME", "pattern": [{"LOWER": "who"}, {"LOWER": "are"}, {"LOWER": "you"}]},
    {"label": "NAME", "pattern": [{"LOWER": "your"}, {"LOWER": "name"}]},
    {"label": "AGE", "pattern": [{"LOWER": "how"}, {"LOWER": "old"}, {"LOWER": "are"}, {"LOWER": "you"}]},
    {"label": "AGE", "pattern": [{"LOWER": "your"}, {"LOWER": "age"}]},
    {"label": "CREATOR", "pattern": [{"LOWER": "who"}, {"LOWER": "created"}, {"LOWER": "you"}]},
    {"label": "CREATOR", "pattern": [{"LOWER": "your"}, {"LOWER": "creator"}]},
    {"label": "CREATOR", "pattern": [{"LOWER": "who"}, {"LOWER": "is"}, {"LOWER": "your"}, {"LOWER": "developer"}]},
    {"label": "LOCATION", "pattern": [{"LOWER": "where"}, {"LOWER": "are"}, {"LOWER": "you"}]},
    {"label": "LOCATION", "pattern": [{"LOWER": "your"}, {"LOWER": "location"}]},
    {"label": "LOCATION", "pattern": [{"LOWER": "where"}, {"LOWER": "do"}, {"LOWER": "you"}, {"LOWER": "live"}]},
    {"label": "INTRODUCE", "pattern": [{"LOWER": "my"}, {"LOWER": "name"}, {"LOWER": "is"}, {"LOWER": {"REGEX": ".*"}}]},
    {"label": "HOBBY", "pattern": [{"LOWER": "my"}, {"LOWER": "hobby"}, {"LOWER": "is"}, {"LOWER": {"REGEX": ".*"}}]},
    {"label": "HOBBY", "pattern": [{"LOWER": "i"}, {"LOWER": "like"}, {"LOWER": {"REGEX": ".*"}}]},
    {"label": "FEELING", "pattern": [{"LOWER": "i"}, {"LOWER": "feel"}, {"LOWER": {"REGEX": ".*"}}]},
    {"label": "FEELING", "pattern": [{"LOWER": "i"}, {"LOWER": "am"}, {"LOWER": {"REGEX": ".*"}}]},
]

for pattern in patterns:
    matcher.add(pattern["label"], [pattern["pattern"]])

user_name = ""
user_hobby = ""
user_feeling = ""

def get_response(doc):
    global user_name, user_hobby, user_feeling
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        label = nlp.vocab.strings[match_id]
        if label == "GREET":
            return random.choice(["Hello! How can I help you?", "Hi there! How can I assist you today?", "Hey! How's it going?"])
        elif label == "GREETINGS":
            return random.choice(["I am fine", "I am Good"])
        elif label == "BYE":
            return random.choice(["Goodbye! Have a nice day!", "See you later!", "Bye! Take care!"])
        elif label == "THANKS":
            return random.choice(["You're welcome!", "No problem!", "Anytime!", "You are always welcome"])
        elif label == "NAME":
            return random.choice(["My name is Bot.", "I am Bot, at your service."])
        elif label == "AGE":
            return random.choice(["I am a timeless entity.", "I don't have an age like humans do.", "Bots dont have age"])
        elif label == "CREATOR":
            return random.choice(["The Great Haji Ahmad Luqman.", "The Great Haji Ahmad Luqman"])
        elif label == "LOCATION":
            return random.choice(["I exist in the cloud.", "I am everywhere and nowhere."])
        elif label == "INTRODUCE":
            user_name = span[-1].text
            return f"Nice to meet you, {user_name}! How can I assist you today?"
        elif label == "HOBBY":
            user_hobby = span[-1].text
            return f"That sounds fun, {user_name}! I wish I could try {user_hobby} too."
        elif label == "FEELING":
            user_feeling = span[-1].text
            return f"I'm sorry to hear that you're feeling {user_feeling}, {user_name}. Is there anything I can do to help?"
    return "I'm sorry, I don't understand that."

def startbot():
    print("Hi! I am a Bot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day!")
            break
        doc = nlp(user_input)
        response = get_response(doc)
        print(f"Bot : {response}")

startbot()
