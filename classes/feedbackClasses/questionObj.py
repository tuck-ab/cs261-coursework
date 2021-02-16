import generalFeedbackObj

class Question(generalFeedbackObj.GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, questionText):
        super().__init__(anonFlag, attendeeID)
        self.questionText = questionText
    
    def getQuestionText(self):
        return self.questionText


test = Question(True, 100101, "this is your question")

print(test.getQuestionText())
print(test.getAnon())
print(test.getAttendee())