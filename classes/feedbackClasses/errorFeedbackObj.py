from .generalFeedbackObj import GeneralFeedback

class ErrorFeedback(GeneralFeedback):

    def __init__(self, attendee_id, meeting_id, error_type, error_message):
        super().__init__(attendee_id, meeting_id)
        self.error_type = error_type
        self.error_message = error_message
    
    def get_error_type(self):
        return self.error_type
    
    def get_error_message(self):
        return self.error_message
