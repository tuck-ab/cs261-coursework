from .responseObj import Response

class TextResponse(Response):

    def __init__(self, attendee_id, meeting_id, response_type, response_prompt, response_text):
        super().__init__(attendee_id, meeting_id, response_type, response_prompt)
        self.response_text = response_text
    
    def get_response_text(self):
        return self.response_text
