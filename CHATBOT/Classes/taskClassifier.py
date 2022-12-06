# import necessary packages

class TaskClassifier:
    
    def __init__(self) -> None:
        pass

    def getResponse(self, res):
        """_summary_

        Args:
            res (list): responses and respective probablites

        Returns:
            _type_: tuple of response and its tag
            *This function will  get the response for the predicted tag
            The process happening in this code block is mentioned below:
            1. load the intent file.
            2. select appropriate response from the intent file.
            3. returns resnponse and tag.
        """
        try:
            "code here"
        except:
            "call log module for writing log"

	
    def response(self, phrase):
        """_summary_

        Args:
            phrase (string): user input
            *This function will redirect to the respective task. classify the user input by calling queryFiltering() function.
            The process happening in this code block is mentioned below:
            1. call the queryFiltering() function and identify the task
            2. redirect to the respective task and get response.
            3. call googleSearch() fucntion or scrape() function or getWeather() or self learning method based on the user input.
        """
        try:
            "code here"
        except:
            "call log module for writing log"