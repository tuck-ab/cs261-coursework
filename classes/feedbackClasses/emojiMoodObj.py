from .moodObj import Mood

class EmojiMood(Mood):

    def __init__(self, attendee_id, meeting_id, mood_type, mood_score, mood_time, current_mood_avg, mood_emoji):
        super().__init__(attendee_id, meeting_id, mood_type, mood_score, mood_time, current_mood_avg)
        self.mood_emoji = mood_emoji
    
    def get_mood_emoji(self):
        return self.mood_emoji

    def set_emoji_mood_score(self, score):
        self.mood_score = score
        return self.mood_score
