class GeneralPrompt:

    def __init__(self, hostID, promptText):
        self.hostID = hostID
        self.promptText = promptText
    
    def getHost(self):
        return self.hostID

    def getPromptText(self):
        return self.promptText
