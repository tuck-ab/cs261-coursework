from .responseObj import Response

class MultChoiceResponse(Response):

    def __init__(self, anonFlag, attendeeID, meetingID, responseType, responsePrompt, responseChoice):
        super().__init__(anonFlag, attendeeID, meetingID, responseType, responsePrompt)
        self.responseChoice = responseChoice
    
    def getResponseChoice(self):
        return self.responseChoice
