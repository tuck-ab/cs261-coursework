from .moodObj import Mood

class EmojiMood(Mood):

    def __init__(self, anonFlag, attendeeID, meetingID, moodType, moodScore, moodTime, moodEmoji):
        super().__init__(anonFlag, attendeeID, meetingID, moodType, moodScore, moodTime)
        self.moodEmoji = moodEmoji
    
    def getMoodEmoji(self):
        return self.moodEmoji

    def setEmojiMoodScore(self, score):
        self.moodScore = score
        return self.moodScore
