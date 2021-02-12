from .attendee import Attendee

class Meeting:
    def __init__(self, token):
        self.code = self.generate_code()
        self.host_token = token

        self.host_room = token + "_h"
        self.attendee_room = token + "_a"

        self.data = None

        self.host = None 
        self.attendees = set()

    def attendee_in_meeting(self, attendee):
        pass

    def add_attendee(self, sid):
        new_attendee = Attendee(sid)
        self.attendees.add(new_attendee)

    def get_attendee(self):
        pass 

    # def send_to_attendees(self, data):
    #     for attendee in self.attendees:
    #         attendee.send(data)

    def set_host(self, host):
        pass 

    def get_host(self):
        pass

    def generate_code(self):
        return "123"

    def __str__(self):
        out_str = "\nMeeting:\n"
        out_str += "  Code: " + str(self.code)
        out_str += "\n\n"
        return out_str