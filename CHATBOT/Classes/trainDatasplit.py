import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
from nltk.tokenize import word_tokenize
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

import dataPreprocessing as dp
from dataPreprocessing import *
print("start")
class trainDataSplit:
    def set_variables(self):
        self.classes=dp.d.classes      
        self.words=dp.d.words
        self.doc=dp.d.doc
    def train(self):
        self.set_variables()
        training=[]
        output_empty = [0] * len(self.classes)
        for d in self.doc:
            bag=[]
            pattern_words=d[0]
            pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
            for w in self.words:
                bag.append(1) if w in pattern_words else bag.append(0)
            output_row=list(output_empty)
            output_row[(self.classes).index(d[1])]=1
            training.append([bag,output_row])
        random.shuffle(training)
        training=np.array(training)
        self.train_x = list(training[:,0])
        self.train_y = list(training[:,1])
        print("Training data created")
        print (self.train_x)

g=trainDataSplit()
g.train()
print("finish")