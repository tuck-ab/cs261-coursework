from .generalPromptObj import GeneralPrompt

class EmojiPrompt(GeneralPrompt):

    def __init__(self, hostID, meetingID, promptText, allowedEmojis = list()):
        super().__init__(hostID, meetingID, promptText)
        self.allowedEmojis = allowedEmojis
    
    def getAllowedEmojis(self):
        return self.allowedEmojis

    def addEmoji(self,emoji):
        self.allowedEmojis.append(emoji)
    
    def removeEmoji(self,emoji):
        self.allowedEmojis.remove(emoji)
