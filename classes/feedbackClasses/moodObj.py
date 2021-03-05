from .generalFeedbackObj import GeneralFeedback

class Mood(GeneralFeedback):

    def __init__(self, anonFlag, attendeeID, meetingID, moodType, moodScore, moodTime, current_mood_avg):
        super().__init__(anonFlag, attendeeID, meetingID)
        self.moodType = moodType
        self.moodScore = moodScore
        self.moodTime = moodTime
        self.current_mood_avg = current_mood_avg
    
    def getMoodType(self):
        return self.moodType
        
    def getMoodScore(self):
        return self.moodScore
    
    def getMoodTime(self):
        return self.moodTime
    
    def get_current_mood_avg(self):
        return self.current_mood_avg
    
