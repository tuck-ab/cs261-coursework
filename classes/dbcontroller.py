# TODO: 
# Define function to insert response
# Ask about including a 'time of mood' attribute to mood feedback


import sqlite3

from .feedbackClasses import *

class DBController:

    # Establishes DB connection and a cursor
    def __init__(self):
        try:
            self.conn = sqlite3.connect('live_feedback.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print("Failed to open database connection", error)

    # Closes DB connection
    def close(self):
        self.conn.close()

    # Helper function to retrieve common attributes among all feedback types
    def getGeneralAttributes(self, feedbackObj):
        meeting = feedbackObj.getMeeting()
        anonBool = feedbackObj.getAnon()
        if anonBool == True:
            anon = 1
        else:
            anon = 0
        attendee = feedbackObj.getAttendee()
        return (meeting, anon, attendee)

    # Helper function to insert a general feedback type
    def insertFeedback(self, meeting, attendee, ftype, anon):
        try:
            self.cursor.execute("INSERT INTO feedback VALUES (NULL, :m, :a, :t, :n)",{'m':meeting, 'a':attendee, 't':ftype, 'n':anon})
            self.cursor.execute("SELECT last_insert_rowid()")
            return self.cursor.fetchone()[0]
        except sqlite3.Error as error:
            return error

    # Inserts an error feedback
    def insertError(self, errorFeedback):
        (meeting, anon, attendee) = self.getGeneralAttributes(errorFeedback)
        errType = errorFeedback.getErrorType()
        errMsg = errorFeedback.getErrorMessage()

        feedback = self.insertFeedback(meeting, attendee, "error", anon)

        if type(feedback) is int:
            try:
                self.cursor.execute("INSERT INTO errors VALUES (:f, :t, :m)",{'f':feedback, 't':errType, 'm':errMsg})
                self.conn.commit()
            except sqlite3.Error as error:
                print("Error inserting into table errors:", error)
                self.conn.rollback()
        else:
            print("Error inserting into table feedback:", feedback)
            self.conn.rollback()

    # Inserts a question feedback
    def insertQuestion(self, question):
        (meeting, anon, attendee) = self.getGeneralAttributes(question)
        qstnMsg = question.getQuestionText()

        feedback = self.insertFeedback(meeting, attendee, "question", anon)

        if type(feedback) is int:
            try:
                self.cursor.execute("INSERT INTO questions VALUES (:f, :m)",{'f':feedback, 'm':qstnMsg})
                self.conn.commit()
            except sqlite3.Error as error:
                print("Error inserting into table questions:", error)
                self.conn.rollback()
        else:
            print("Error inserting into table feedback:", feedback)
            self.conn.rollback()

    # Helper function to insert a general mood feedback
    def insertGeneralMood(self, feedback, moodType, score):
        try:
            self.cursor.execute("INSERT INTO moods VALUES (NULL, :f, :t, :s, :l)",{'f':feedback, 't':moodType, 's':score, 'l':12})
            self.cursor.execute("SELECT last_insert_rowid()")
            return self.cursor.fetchone()[0]
        except sqlite3.Error as error:
            return error

    # Insert a mood feedback
    def insertMood(self, mood):
        (meeting, anon, attendee) = self.getGeneralAttributes(mood)
        moodType = mood.getMoodType()
        score = mood.getMoodScore()

        if moodType == "text" or moodType == "emoji":
            feedback = self.insertFeedback(meeting, attendee, "mood", anon)
            if type(feedback) is int:
                moodID = self.insertGeneralMood(feedback, moodType, score) # time of mood?
                if type(moodID) is int:
                    if moodType == "text":
                        txt_msg = mood.getMoodText()
                        try:
                            self.cursor.execute("INSERT INTO text_moods VALUES (:m, :t)",{'m':moodID, 't':txt_msg})
                            self.conn.commit()
                        except sqlite3.Error as error:
                            print("Error inserting into table text_moods:", error)
                            self.conn.rollback()
                    else:
                        emj_type = mood.getMoodEmoji()
                        try:
                            self.cursor.execute("INSERT INTO emoji_moods VALUES (:m, :t)",{'m':moodID, 't':emj_type})
                            self.conn.commit()
                        except sqlite3.Error as error:
                            print("Error inserting into table emoji_moods:", error)
                            self.conn.rollback()
                else:
                    print("Error inserting into table moods:", moodID)
                    self.conn.rollback()
            else:
                print("Error inserting into table feedback:", feedback)
                self.conn.rollback()
        else:
            print("Invalid mood type:", moodType)

    # Create an event for a host
    def createEvent(self, host, title):
        table = "hosts"
        meeting = -1
        try:
            self.cursor.execute("SELECT hostid FROM hosts WHERE hostid = :h",{'h':host})
            if not self.cursor.fetchone():
               self.cursor.execute("INSERT INTO hosts VALUES (:h)",{'h':host})
            table = "meetings"
            self.cursor.execute("INSERT INTO meetings VALUES (NULL, :h, :t, :r)",{'h':host, 't':title, 'r':121})
            self.cursor.execute("SELECT last_insert_rowid()")
            meeting = self.cursor.fetchone()[0]
            self.conn.commit()
        except sqlite3.Error as error:
            print("Error inserting into table",table,":",error)
            self.conn.rollback()
        finally:
            return meeting

    # Add attendee to an event
    def addAttendee(self, attendee, meeting):
        try:
            self.cursor.execute("INSERT INTO attendees VALUES (:a, :m)",{'a':attendee, 'm':meeting})
            self.conn.commit()
        except sqlite3.Error as error:
            print("Error inserting into table attendees:",error)