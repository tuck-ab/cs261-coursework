import random

from .meeting import Meeting
from ..dbcontroller import *

class Meeting_Controller:
    def __init__(self):
        self.meetings_by_token = {}
        self.meetings_by_code = {}

    def create_meeting(self, db_conn):
        token = self.generate_host_token(db_conn)
        code = self.generate_join_code()

        new_meeting = Meeting(token, code)

        self.meetings_by_token[token] = new_meeting
        self.meetings_by_code[code] = new_meeting

        return new_meeting

    def end_meeting(self, meeting):
        self.meetings_by_code.remove(meeting)
        self.meetings_by_token.remove(meeting)

    def generate_host_token(self, db_conn):
        while True:
            token = str(random.randint(1000,9999))
            if db_conn.unique_token(token):
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

    def get_meeting_from_host(self, host):
        for meeting in self.meetings_by_token.values():
            if meeting.get_host() == host:
                return meeting

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

    def get_host_from_sid(self, sid):
        for meeting in self.meetings_by_token.values():
            if meeting.get_host().get_sid() == sid:
                return meeting.get_host()
