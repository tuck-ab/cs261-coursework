from .responseObj import Response

class TextResponse(Response):

    def __init__(self, anonFlag, attendeeID, meetingID, responseType, responsePrompt, responseText):
        super().__init__(anonFlag, attendeeID, meetingID, responseType, responsePrompt)
        self.responseText = responseText
    
    def getResponseText(self):
        return self.responseText
