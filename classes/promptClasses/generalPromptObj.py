class GeneralPrompt:

    def __init__(self, hostID, meetingID, promptText):
        self.hostID = hostID
        self.promptText = promptText
        self.meetingID = meetingID
    
    def getHost(self):
        return self.hostID

    def getPromptText(self):
        return self.promptText
    
    def getMeeting(self):
        return self.meetingID
