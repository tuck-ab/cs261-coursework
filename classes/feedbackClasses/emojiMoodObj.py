import moodObj

class EmojiMood(moodObj.Mood):

    def __init__(self, anonFlag, attendeeID, moodScore, moodEmoji):
        super().__init__(anonFlag, attendeeID, moodScore)
        self.moodEmoji = moodEmoji
    
    def getMoodEmoji(self):
        return self.moodEmoji

    def setEmojiMoodScore(self, score):
        print("we are now setting a new mood score")
        self.moodScore = score
        return self.moodScore


test = EmojiMood(True, 100101, 0.7, "this is the emoji")

print(test.getMoodScore())
print(test.getAnon())
print(test.getAttendee())
print(test.getMoodEmoji())
print(test.setEmojiMoodScore(0.8))