
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
from nltk.tokenize import word_tokenize
import numpy as np
import random
import __init__
from __init__ import *
class f:
    def set_variables(self):
        self.words=__init__.t.words
        self.classes=__init__.t.classes
        self.doc=__init__.t.doc
        self.intents=__init__.t.intents
        self.ignore_words=__init__.t.ignore_words
    def processing(self):
        self.set_variables()
        for i in self.intents: #or self.intente["intents"] but then change line 18
            for p in i['patterns']:
                w = nltk.word_tokenize(p)
                self.words.extend(w)
                self.doc.append((w,i["tag"]))
                if i["tag"] not in self.classes:
                    self.classes.append(i["tag"])
        self.words=[lemmatizer.lemmatize(w.lower()) for w in self.words if w not in self.ignore_words]
        self.words = sorted(list(set(self.words)))
        self.classes = sorted(list(set(self.classes)))
        print (len(self.doc), "documents")
        print (len(self.classes), "classes", self.classes)
        print (len(self.words), "unique lemmatized words", self.words)
        file1=open('words.pkl','wb')
        file2=open('classes.pkl','wb')
        pickle.dump(self.words,file1)
        pickle.dump(self.classes,file2)
d=f()
d.processing()

words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

class gui_processing:
    def clean_up_sentence(self,sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words
    def bow(self, sentence, words, show_details=True):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0]*len(words) 
        for s in sentence_words:
            for i,w in enumerate(words):
                if w == s: 
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        return(np.array(bag))
c=gui_processing()

