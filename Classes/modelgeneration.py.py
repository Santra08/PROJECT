from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
from keras.models import load_model


import trainDatasplit as tds
from trainDatasplit import *

import dataPreprocessing as dp
from dataPreprocessing import *
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
intents = json.loads(open(r'C:\Users\abhishek\Desktop\CHATBOT\intents-1.json').read())
#remember to change intents file in init


import tkinter
from tkinter import *

class model:
    def set_variables(self):
        self.x_train=tds.g.train_x
        self.y_train=tds.g.train_y
    def model_creation(self):
        self.set_variables()
        model = Sequential()
        model.add(Dense(128, input_shape=(len(self.x_train[0]),), activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(len(self.y_train[0]), activation='softmax'))
        # Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
        sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
        hist = model.fit(np.array(self.x_train), np.array(self.y_train), epochs=200, batch_size=5, verbose=1)
        model.save('chatbot_model.h6', hist)
        print("model created")
        
        
 class gui_model:
    def chatbot_response(self,text):
        ints= self.predict_class(text, model)
        res = self.getResponse(ints,intents)
        return res
    def predict_class(self, sentence, model):
        words = pickle.load(open('words.pkl','rb'))
        p=dp.c.bow(sentence, words,show_details=False)
        model = load_model('chatbot_model.h6')
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
        return return_list
    def getResponse(self,ints,intents_json):
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                break
        return result
    
m=model()
m.model_creation()

gui=gui_model()

print("finished")

import __init__
from __init__ import *
class create_gui:
    def __init__(self):
        self.base=Tk()
        self.main_window()
    #run window
    def run(self):
        self.base.mainloop()
    def main_window(self):
        self.base.title("chat")
        self.base.geometry("400x500")
        self.base.resizable(width=FALSE, height=FALSE)
        self.chat_window()
    def send(self):
        print("send")
        msg = self.EntryBox.get("1.0",'end-1c').strip()
        self.EntryBox.delete("0.0",END)
        if msg != '':
            self.ChatLog.config(state=NORMAL)
            self.ChatLog.insert(END, "You: " + msg + '\n\n')
            self.ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
            res = gui.chatbot_response(msg)
            self.ChatLog.insert(END, "Bot: " + res + '\n\n')
            self.ChatLog.config(state=DISABLED)
            self.ChatLog.yview(END)
    def chat_window(self):
        print("create chat window")
        self.ChatLog = Text(self.base, bd=0, bg="white", height="8", width="50", font="Arial",)
        self.ChatLog.config(state=DISABLED)
        #Bind scrollbar to Chat window
        self.scrollbar = Scrollbar(self.base, command=self.ChatLog.yview, cursor="heart")
        self.ChatLog['yscrollcommand'] = self.scrollbar.set
        #create send button
        self.SendButton = Button(self.base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= self.send)
        print("going to entry box")
        self.EntryBox = Text(self.base, bd=0, bg="white",width="29", height="5", font="Arial")    
        self.scrollbar.place(x=376,y=6, height=386)
        self.ChatLog.place(x=6,y=6, height=386, width=370)
        self.EntryBox.place(x=128, y=401, height=90, width=265)
        self.SendButton.place(x=6, y=401, height=90)
        print("finish entry")
        self.run()
c_gui=create_gui()
