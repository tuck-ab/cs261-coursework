import sqlite3

from feedbackClasses import *

class DBController:

    def __init__(self):
        self.conn = sqlite3.connect('~/cs261-coursework/live_feedback.db')
        self.cursor = conn.cursor()

    def close(self):
        self.conn.close()

    def insertFeedback(self, meeting, attendee, ftype, anon):

        self.cursor.execute("INSERT INTO feedback VALUES (:meeting, :attendee, :type, :anon)",{'meeting':meeting, 'attendee':attendee, 'type':ftype, 'anon':anon})
        self.conn.commit()

        self.cursor.execute("SELECT last_insert_rowid()")
        return self.cursor.fetchone()


    def insertError(self, errorFeedbackObj):
        meeting = 420
        anonB = errorFeedbackObj.getAnon
        if anonB == True:
            anon = 1
        else:
            anon = 0
        attendee = errorFeedbackObj.getAttendee
        errType = errorFeedbackObj.getErrorType
        errMsg = errorFeedbackObj.getErrorMessage

        feedback = self.insertFeedback(meeting, attendee, "Error", anon)

        self.cursor.execute("INSERT INTO errors VALUES (:feedback, :type, :msg)",{'feedback':feedback, 'type':errType, 'msg':errMsg})
        self.conn.commit()
