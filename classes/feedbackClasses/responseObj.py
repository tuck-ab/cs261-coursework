import generalFeedbackObj

class Response(generalFeedbackObj.GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, responsePrompt):
        super().__init__(anonFlag, attendeeID)
        self.responsePrompt = responsePrompt
    
    def getResponsePrompt(self):
        return self.responsePrompt


test = Response(True, 100101, "this is your prompt")

