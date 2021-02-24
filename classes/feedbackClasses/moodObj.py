from .generalFeedbackObj import GeneralFeedback

class Mood(GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, meetingID, moodType, moodScore):
        super().__init__(anonFlag, attendeeID, meetingID)
        self.moodType = moodType
        self.moodScore = moodScore
    
    def getMoodType(self):
        return self.moodType
        
    def getMoodScore(self):
        return self.moodScore
