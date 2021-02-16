import generalFeedbackObj

class Mood(generalFeedbackObj.GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, moodScore):
        super().__init__(anonFlag, attendeeID)
        self.moodScore = moodScore
    
    def getMoodScore(self):
        return self.moodScore