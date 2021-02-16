import generalFeedbackObj

class ErrorFeedback(generalFeedbackObj.GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, errorType, errorMessage):
        super().__init__(anonFlag, attendeeID)
        self.errorType = errorType
        self.errorMessage = errorMessage
    
    def getErrorType(self):
        return self.errorType
    
    def getErrorMessage(self):
        return self.errorMessage


test = ErrorFeedback(True, 100101, 2, "we cant hear u")

print(test.getErrorMessage())
print(test.getErrorType())
print(test.getAnon())
print(test.getAttendee())