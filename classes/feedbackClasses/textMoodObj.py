from .moodObj import Mood

class TextMood(Mood):

    def __init__(self, attendee_id, meeting_id, mood_type, mood_score, mood_time, current_mood_avg, mood_text):
        super().__init__(attendee_id, meeting_id, mood_type, mood_score, mood_time, current_mood_avg)
        self.mood_text = mood_text
    
    def get_mood_text(self):
        return self.mood_text

    def set_text_mood_score(self, score):
        self.mood_score = score
        return self.mood_score
