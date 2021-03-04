from .attendee import Attendee
from ..sentiment import Sentiment

class Meeting:
    def __init__(self, token, code):
        self.host_token = token
        self.code = code
        self.title = ""

        self.host_room = token + "_h"
        self.attendee_room = token + "_a"

        self.template = None

        self.host = None
        self.attendees = {}
        
        self.sentimentAnalyser = Sentiment(0,0,0,0,0,"")

    def getSentimentAnalyser(self):
        return self.sentimentAnalyser
        
    def set_template(self, template):
        self.template = template

    def get_template(self):
        return self.template

    def attendee_in_meeting(self, attendee):
        pass

    def add_attendee(self, attendee):
        self.attendees[attendee.sid] = attendee

    def get_attendee(self, sid):
        if sid in self.attendees:
            return self.attendees[sid]
        else:
            return None

    def set_host(self, host):
        self.host = host

    def get_host(self):
        if self.host == None:
            print("Host has not been set yet")

        return self.host
    
    def get_token(self):
        return self.host_token

    def __str__(self):
        out_str = "\nMeeting:\n"
        out_str += "  Code: " + str(self.code)
        out_str += "\n\n"
        return out_str