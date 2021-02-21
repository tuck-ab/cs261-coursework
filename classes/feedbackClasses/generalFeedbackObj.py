class GeneralFeedback:

    def __init__(self, anonFlag, attendeeID, meetingID):
        self.anonFlag = anonFlag
        self.attendeeID = attendeeID
        self.meetingID = meetingID
    
    def getAnon(self):
        return self.anonFlag

    def getAttendee(self):
        return self.attendeeID

    def getMeeting(self):
        return self.meetingID
    
