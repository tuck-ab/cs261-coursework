from .generalFeedbackObj import GeneralFeedback

class QuestionFeedback(GeneralFeedback):

    def __init__(self, attendee_id, meeting_id, question_text):
        super().__init__(attendee_id, meeting_id)
        self.question_text = question_text
    
    def get_question_text(self):
        return self.question_text
