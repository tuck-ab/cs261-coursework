from .meeting import Meeting

class Controller:
    def __init__(self):
        self.meetings = {}

    def create_meeting(self):
        token = self.generate_host_token()
        new_meeting = Meeting(token)

        self.meetings[token] = new_meeting

        return new_meeting

    def generate_host_token(self):
        return "321"

    def get_meeting_from_attendee(self):
        pass

    def get_meeting_from_host(self):
        pass

    def get_meeting_from_token(self, token):
        return self.meetings[token]

    def host_disconnect(self):
        pass 

    def client_disconnect(self):
        pass

