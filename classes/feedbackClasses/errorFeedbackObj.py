from .generalFeedbackObj import GeneralFeedback

class ErrorFeedback(GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, meetingID, errorType, errorMessage):
        super().__init__(anonFlag, attendeeID, meetingID)
        self.errorType = errorType
        self.errorMessage = errorMessage
    
    def getErrorType(self):
        return self.errorType
    
    def getErrorMessage(self):
        return self.errorMessage
