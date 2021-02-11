class GeneralFeedback:

    def __init__(self, anonFlag, attendeeID):
        self.anonFlag = anonFlag
        self.attendeeID = attendeeID
    
    def getAnon(self):
        return self.anonFlag

    def getAttendee(self):
        return self.attendeeID
