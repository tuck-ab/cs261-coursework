from .responseObj import Response

class TextResponse(Response):

    def __init__(self, anonFlag, attendeeID, meetingID, responsePrompt, responseText):
        super().__init__(anonFlag, attendeeID, meetingID, responsePrompt)
        self.responseText = responseText
    
    def getResponseText(self):
        return self.responseText
