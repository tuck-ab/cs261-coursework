class Attendee:
    def __init__(self, connection):
        self.connection = connection

    def send(self, data):
        self.connection.emit("attendee_update", data)