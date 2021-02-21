from .moodObj import Mood

class TextMood(Mood):

    def __init__(self, anonFlag, attendeeID, meetingID, moodScore, moodText):
        super().__init__(anonFlag, attendeeID, meetingID, moodScore)
        self.moodText = moodText
    
    def getMoodText(self):
        return self.moodText

    def setTextMoodScore(self, score):
        print("we are now setting a new mood score")
        self.moodScore = score
        return self.moodScore
