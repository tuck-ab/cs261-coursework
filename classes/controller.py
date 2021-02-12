from .meeting import Meeting

class Controller:
    def __init__(self):
        self.meetings_by_token = {}
        self.meetings_by_code = {}

    def create_meeting(self):
        token = self.generate_host_token()
        new_meeting = Meeting(token)

        self.meetings_by_token[token] = new_meeting
        self.meetings_by_code[new_meeting.code] = new_meeting

        return new_meeting

    def generate_host_token(self):
        return "321"

    def get_meeting_from_attendee(self):
        pass

    def get_meeting_from_host(self):
        pass

    def get_meeting_from_token(self, token):
        if token in self.meetings_by_token:
            return self.meetings_by_token[token]
        else:
            return None

    def get_meeting_from_code(self, code):
        if code in self.meetings_by_code:
            return self.meetings_by_code[code]
        else:
            return None

    def host_disconnect(self):
        pass 

    def client_disconnect(self):
        pass

