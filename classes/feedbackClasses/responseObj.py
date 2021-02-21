from .generalFeedbackObj import GeneralFeedback

class Response(GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, meetingID, responsePrompt):
        super().__init__(anonFlag, attendeeID, meetingID)
        self.responsePrompt = responsePrompt
    
    def getResponsePrompt(self):
        return self.responsePrompt
