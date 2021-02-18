from .responseObj import Response

class EmojiResponse(responseObj.Response):

    def __init__(self, anonFlag, attendeeID, responsePrompt, responseEmoji):
        super().__init__(anonFlag, attendeeID, responsePrompt)
        self.responseEmoji = responseEmoji
    
    def getResponseEmoji(self):
        return self.responseEmoji
