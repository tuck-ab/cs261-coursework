from .generalFeedbackObj import GeneralFeedback

class Mood(GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, meetingID, moodType, moodScore, moodTime):
        super().__init__(anonFlag, attendeeID, meetingID)
        self.moodType = moodType
        self.moodScore = moodScore
        self.moodTime = moodTime
    
    def getMoodType(self):
        return self.moodType
        
    def getMoodScore(self):
        return self.moodScore
    
