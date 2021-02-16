import responseObj

class TextResponse(responseObj.Response):

    def __init__(self, anonFlag, attendeeID, responsePrompt, responseText):
        super().__init__(anonFlag, attendeeID, responsePrompt)
        self.responseText = responseText
    
    def getResponseText(self):
        return self.responseText


test = TextResponse(True, 100101, "this is your prompt", "this is your response")

print(test.getResponseText())
print(test.getResponsePrompt())
print(test.getAnon())
print(test.getAttendee())