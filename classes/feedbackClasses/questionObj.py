import generalFeedbackObj

class Question(generalFeedbackObj.GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, questionText):
        super().__init__(anonFlag, attendeeID)
        self.questionText = questionText
    
    def getQuestionText(self):
        return self.questionText
