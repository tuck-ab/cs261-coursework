from .generalFeedbackObj import GeneralFeedback

class Mood(GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, meetingID, moodScore):
        super().__init__(anonFlag, attendeeID, meetingID)
        self.moodScore = moodScore
    
    def getMoodScore(self):
        return self.moodScore
