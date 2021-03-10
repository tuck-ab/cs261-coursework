from .responseObj import Response

class EmojiResponse(Response):

    def __init__(self, attendee_id, meeting_id, response_type, response_prompt, response_emoji):
        super().__init__(attendee_id, meeting_id, response_type, response_prompt)
        self.response_emoji = response_emoji
    
    def get_response_emoji(self):
        return self.response_emoji
