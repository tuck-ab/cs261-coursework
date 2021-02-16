import moodObj

class TextMood(moodObj.Mood):

    def __init__(self, anonFlag, attendeeID, moodScore, moodText):
        super().__init__(anonFlag, attendeeID, moodScore)
        self.moodText = moodText
    
    def getMoodText(self):
        return self.moodText

    def setTextMoodScore(self, score):
        print("we are now setting a new mood score")
        self.moodScore = score
        return self.moodScore


test = TextMood(True, 100101, 0.7, "this is the text")

print(test.getMoodScore())
print(test.getAnon())
print(test.getAttendee())
print(test.getMoodText())
print(test.setTextMoodScore(0.8))