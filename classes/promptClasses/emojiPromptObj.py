import generalPromptObj

class EmojiPrompt(generalPromptObj.GeneralPrompt):

    def __init__(self, hostID, promptText, allowedEmojis = list()):
        super().__init__(hostID, promptText)
        self.allowedEmojis = allowedEmojis
    
    def getAllowedEmojis(self):
        return self.allowedEmojis

    def addEmoji(self,emoji):
        self.allowedEmojis.append(emoji)
    
    def removeEmoji(self,emoji):
        self.allowedEmojis.remove(emoji)


testList = [1,3,5,6]
test = EmojiPrompt(1010101, "this is the text", testList)

print(test.getAllowedEmojis())
test.addEmoji(2)
print(test.getAllowedEmojis())
test.removeEmoji(3)
print(test.getAllowedEmojis())
