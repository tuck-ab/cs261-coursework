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
