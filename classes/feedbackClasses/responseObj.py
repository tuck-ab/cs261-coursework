from .generalFeedbackObj import GeneralFeedback

class Response(GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, meetingID, responseType, responsePrompt):
        super().__init__(anonFlag, attendeeID, meetingID)
        self.responseType = responseType
        self.responsePrompt = responsePrompt
    
    def getResponseType(self):
        return self.responseType
        
    def getResponsePrompt(self):
        return self.responsePrompt
