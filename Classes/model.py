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