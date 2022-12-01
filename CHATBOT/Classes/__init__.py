
import json
class initialise:
    def __init__(self):
        self.words=[]
        self.classes=[]
        self.doc=[]
        self.ignore_words = ['?', '!','(',')']
        data_file = open(r"C:\Users\santr\Desktop\santra kujnni\CHATBOT\intents-1.json").read()
        self.intents = json.loads(data_file)['intents']
print("safdfasd")
t=initialise()