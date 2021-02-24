import random

from .meeting import Meeting

class Meeting_Controller:
    def __init__(self):
        self.meetings_by_token = {}
        self.meetings_by_code = {}

    def create_meeting(self):
        token = self.generate_host_token()
        code = self.generate_join_code()

        new_meeting = Meeting(token, code)

        self.meetings_by_token[token] = new_meeting
        self.meetings_by_code[code] = new_meeting

        return new_meeting

    def generate_host_token(self):
        ## TODO This needs to be changed to make sure it is a completely new
        ##      token, this will involve accessing the database
        while True:
            token = str(random.randint(1000,9999))
            if not token in self.meetings_by_token:
                return token

    def generate_join_code(self):
        while True:
            code = str(random.randint(1000,9999))
            if not code in self.meetings_by_code:
                return code

    def get_attendee(self, sid):
        for meeting in self.meetings_by_token.values():
            result = meeting.get_attendee(sid)
            if result != None:
                return result

        return None

    def get_meeting_from_attendee(self, sid):
        for meeting in self.meetings_by_token.values():
            result = meeting.get_attendee(sid)
            if result != None:
                return meeting

        return None

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

    def attendee_disconnect(self):
        pass

