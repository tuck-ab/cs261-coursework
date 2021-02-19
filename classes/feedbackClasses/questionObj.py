from .generalFeedbackObj import GeneralFeedback

class Question(GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, meetingID, questionText):
        super().__init__(anonFlag, attendeeID, meetingID)
        self.questionText = questionText
    
    def getQuestionText(self):
        return self.questionText
