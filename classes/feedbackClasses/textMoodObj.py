from .moodObj import Mood

class TextMood(Mood):

    def __init__(self, anonFlag, attendeeID, meetingID, moodType, moodScore, moodTime, current_mood_avg, moodText):
        super().__init__(anonFlag, attendeeID, meetingID, moodType, moodScore, moodTime, current_mood_avg)
        self.moodText = moodText
    
    def getMoodText(self):
        return self.moodText

    def setTextMoodScore(self, score):
        self.moodScore = score
        return self.moodScore
