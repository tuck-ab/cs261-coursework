from .responseObj import Response

class TextResponse(responseObj.Response):

    def __init__(self, anonFlag, attendeeID, responsePrompt, responseText):
        super().__init__(anonFlag, attendeeID, responsePrompt)
        self.responseText = responseText
    
    def getResponseText(self):
        return self.responseText
