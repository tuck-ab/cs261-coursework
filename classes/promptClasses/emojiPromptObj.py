from .generalPromptObj import GeneralPrompt

class EmojiPrompt(GeneralPrompt):

    def __init__(self, host_id, meeting_id, prompt_text, allowed_emojis = list()):
        super().__init__(host_id, meeting_id, prompt_text)
        self.allowed_emojis = allowed_emojis
    
    def get_allowed_emojis(self):
        return self.allowed_emojis

    def add_emoji(self,emoji):
        self.allowed_emojis.append(emoji)
    
    def remove_emoji(self,emoji):
        self.allowed_emojis.remove(emoji)
