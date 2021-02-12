class Meeting:
    def __init__(self, token):
        self.code = self.generate_code()
        self.host_token = token

        self.data = None

        self.host = None 
        self.attendees = set()

    def attendee_in_meeting(self, attendee):
        pass

    def add_attendee(self, attendee):
        pass 

    def get_attendee(self):
        pass 

    def set_host(self, host):
        pass 

    def get_host(self):
        pass

    def generate_code(self):
        return "123"