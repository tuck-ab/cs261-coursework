from .responseObj import Response

class MultChoiceResponse(Response):

    def __init__(self, attendee_id, meeting_id, response_type, response_prompt, response_answer):
        super().__init__(attendee_id, meeting_id, response_type, response_prompt)
        self.response_answer = response_answer
    
    def get_response_answer(self):
        return self.response_answer
