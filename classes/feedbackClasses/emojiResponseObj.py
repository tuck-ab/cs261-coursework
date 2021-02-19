from .responseObj import Response

class EmojiResponse(Response):

    def __init__(self, anonFlag, attendeeID, meetingID, responsePrompt, responseEmoji):
        super().__init__(anonFlag, attendeeID, meetingID, responsePrompt)
        self.responseEmoji = responseEmoji
    
    def getResponseEmoji(self):
        return self.responseEmoji
