# import necessary packages

class PredictionModel:
    
    def __init__(self) -> None:
        pass

    def preprocess(self, phrase):
        """_summary_

        Args:
            phrase (string): user input

        Returns:
            _type_: list of formatted words

            *This function will  preprocess the user input
            The process happening in this code block is mentioned below:
            1. Tokenisation
            2. Lemmatisation
            3. Store the preprocessed data into a list.
        """
        try:
            "code here"
        except:
            "call log module for writing log"


    def bagOfWords(self, phrase,words):
        """_summary_

        Args:
            phrase (string): user input
            words (list): preprocessed user input

        Returns:
            _type_: numpy array
            *This function will  generate the bag of words related to the user input
            The process happening in this code block is mentioned below:
            1. load preprocessed user input.
            2. create the bag of words algorithm.
            3. convert the bag of words into numpy arrays. 


        """
        try:
            "code here"
        except:
            "call log module for writing log"

    def predictCoversation(self, phrase):
        """_summary_

        Args:
            phrase (string): user input

        Returns:
            _type_: list of tag and data

            *This function will  generate response from the model related to the user input. this function will call the bagOfWords() function for response prediction
            The process happening in this code block is mentioned below:
            1. load the model
            2. load trained data(pickle file)
            3. Generate Bot response depends on the tag predicted by choosing appropriate threshold
        """
        try:
            "code here"
        except:
            "call log module for writing log"
