# import necessary packages

# download necessary dependencies
class CommonHandler:

    def __init__(self) -> None:
        pass


    def queryFiltering(self, a):
        """_summary_

        Args:
            phrase (_type_:text): user input

        Returns:
            _type_: List
            
            *This function will identify the category of user input and decide whether the self learning method or rule based method to be applied.
            The process happening in this code block is mentioned below:
            1. Tokenizaton
            2. POS tagging
            3. Based on the POS, the tokens will be stored in respective list.
            4. Lemmatisationa
            5. Classify the user input and divert to task which will give an ideal response(Note: consider POS)
        """
        try:
            " code here"
        except:
            "call log module for writing log"