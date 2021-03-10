from .generalFeedbackObj import GeneralFeedback

class Response(GeneralFeedback):

    def __init__(self, attendee_id, meeting_id, response_type, response_prompt):
        super().__init__(attendee_id, meeting_id)
        self.response_type = response_type
        self.response_prompt = response_prompt
    
    def get_response_type(self):
        return self.response_type
        
    def get_response_prompt(self):
        return self.response_prompt
