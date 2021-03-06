from .responseObj import Response

class MultChoiceResponse(Response):

    def __init__(self, anonFlag, attendeeID, meetingID, responseType, responsePrompt, responseAnswer):
        super().__init__(anonFlag, attendeeID, meetingID, responseType, responsePrompt)
        self.responseAnswer = responseAnswer
    
    def getResponseAnswer(self):
        return self.responseAnswer
