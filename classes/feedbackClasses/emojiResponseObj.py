import responseObj

class EmojiResponse(responseObj.Response):

    def __init__(self, anonFlag, attendeeID, responsePrompt, responseEmoji):
        super().__init__(anonFlag, attendeeID, responsePrompt)
        self.responseEmoji = responseEmoji
    
    def getResponseEmoji(self):
        return self.responseEmoji


test = EmojiResponse(True, 100101, "this is your prompt",4)

print(test.getResponseEmoji())
print(test.getResponsePrompt())
print(test.getAnon())
print(test.getAttendee())