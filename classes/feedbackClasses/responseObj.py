from .generalFeedbackObj import GeneralFeedback

class Response(GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, responsePrompt):
        super().__init__(anonFlag, attendeeID)
        self.responsePrompt = responsePrompt
    
    def getResponsePrompt(self):
        return self.responsePrompt
