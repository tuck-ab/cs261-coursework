from .attendee import Attendee
from ..sentiment import Sentiment
from ..emojisentiment import EmojiSentiment

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
        
        self.sentiment_analyser = Sentiment(0, 0, 0, 0, 0, "")
        
        self.emoji_sentiment_analyser = EmojiSentiment(0, 0, 0, 0, "")

    def get_sentiment_analyser(self):
        return self.sentiment_analyser

    def get_emoji_sentiment_analyser(self):
        return self.emoji_sentiment_analyser

    def set_template(self, template):
        self.template = template

    def get_template(self):
        return self.template

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
        return self.host
    
    def get_token(self):
        return self.host_token

    def __str__(self):
        out_str = "\nMeeting:\n"
        out_str += "  Code: " + str(self.code)
        out_str += "\n\n"
        return out_str