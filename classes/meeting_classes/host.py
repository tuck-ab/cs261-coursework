class Host:
    def __init__(self, sid, meeting=None):
        self.sid = sid 
        self.meeting = meeting

    def set_sid(self, sid):
        self.sid = sid

    def get_sid(self):
        return sid

    def get_room(self):
        return str(self.sid)

    def set_meeting(self, meeting):
        self.meeting = meeting

    def get_meeting(self):
        return self.meeting