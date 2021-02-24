from .moodObj import Mood

class EmojiMood(Mood):

    def __init__(self, anonFlag, attendeeID, meetingID, moodType, moodScore, moodEmoji):
        super().__init__(anonFlag, attendeeID, meetingID, moodType, moodScore)
        self.moodEmoji = moodEmoji
    
    def getMoodEmoji(self):
        return self.moodEmoji

    def setEmojiMoodScore(self, score):
        print("we are now setting a new mood score")
        self.moodScore = score
        return self.moodScore
