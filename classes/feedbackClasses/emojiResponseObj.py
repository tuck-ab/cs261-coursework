from .responseObj import Response

class EmojiResponse(Response):

    def __init__(self, anonFlag, attendeeID, meetingID, responseType, responsePrompt, responseEmoji):
        super().__init__(anonFlag, attendeeID, meetingID, responseType, responsePrompt)
        self.responseEmoji = responseEmoji
    
    def getResponseEmoji(self):
        return self.responseEmoji
