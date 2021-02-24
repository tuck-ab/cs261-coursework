# TODO: Add 'try...except' to catch sqlite3.Error's
# TODO: Add rollback to prevent false inserts

import sqlite3

from .feedbackClasses import *

class DBController:

    def __init__(self):
        try:
            self.conn = sqlite3.connect('live_feedback.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print("Failed to open database connection", error)

    def close(self):
        self.conn.close()

    def getGeneralAttributes(self, feedbackObj):
        meeting = feedbackObj.getMeeting()
        anonBool = feedbackObj.getAnon()
        if anonBool == True:
            anon = 1
        else:
            anon = 0
        attendee = feedbackObj.getAttendee()
        return (meeting, anon, attendee)

    def insertFeedback(self, meeting, attendee, ftype, anon):
        try:
            self.cursor.execute("INSERT INTO feedback VALUES (NULL, :m, :a, :t, :n)",{'m':meeting, 'a':attendee, 't':ftype, 'n':anon})
            self.cursor.execute("SELECT last_insert_rowid()")
            return self.cursor.fetchone()[0]
        except sqlite3.Error as error:
            return error

    def insertError(self, errorFeedback):
        (meeting, anon, attendee) = self.getGeneralAttributes(errorFeedback)
        errType = errorFeedback.getErrorType()
        errMsg = errorFeedback.getErrorMessage()

        feedback = self.insertFeedback(meeting, attendee, "Error", anon)

        if type(feedback) is int:
            try:
                self.cursor.execute("INSERT INTO errors VALUES (:f, :t, :m)",{'f':feedback, 't':errType, 'm':errMsg})
                self.conn.commit()
            except sqlite3.Error as error:
                print("Error inserting into table errors", error)
                self.conn.rollback()
        else:
            print("Error inserting into table feedback", feedback)
            self.conn.rollback()

    def insertQuestion(self, question):
        (meeting, anon, attendee) = self.getGeneralAttributes(question)
        qstnMsg = question.getQuestionText()

        feedback = self.insertFeedback(meeting, attendee, "Question", anon)

        if type(feedback) is int:
            try:
                self.cursor.execute("INSERT INTO questions VALUES (:f, :m)",{'f':feedback, 'm':qstnMsg})
                self.conn.commit()
            except sqlite3.Error as error:
                print("Error inserting into table questions", error)
                self.conn.rollback()
        else:
            print("Error inserting into table feedback", feedback)
            self.conn.rollback()