from .responseObj import Response

class MultChoiceResponse(Response):

    def __init__(self, anonFlag, attendeeID, meetingID, responsePrompt, responseChoice):
        super().__init__(anonFlag, attendeeID, meetingID, responsePrompt)
        self.responseChoice = responseChoice
    
    def getResponseChoice(self):
        return self.responseChoice
