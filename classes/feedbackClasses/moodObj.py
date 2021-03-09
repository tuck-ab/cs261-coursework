from .generalFeedbackObj import GeneralFeedback

class Mood(GeneralFeedback):

    def __init__(self, attendee_id, meeting_id, mood_type, mood_score, mood_time, current_mood_avg):
        super().__init__(attendee_id, meeting_id)
        self.mood_type = mood_type
        self.mood_score = mood_score
        self.mood_time = mood_time
        self.current_mood_avg = current_mood_avg
    
    def get_mood_type(self):
        return self.mood_type
        
    def get_mood_score(self):
        return self.mood_score
    
    def get_mood_time(self):
        return self.mood_time
    
    def get_current_mood_avg(self):
        return self.current_mood_avg
    
