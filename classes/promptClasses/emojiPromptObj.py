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
