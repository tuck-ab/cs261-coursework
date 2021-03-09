class GeneralFeedback:

    def __init__(self, attendee_id, meeting_id):
        self.attendee_id = attendee_id
        self.meeting_id = meeting_id

    def get_attendee(self):
        return self.attendee_id

    def get_meeting(self):
        return self.meeting_id
    
