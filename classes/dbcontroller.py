# TODO:
# Create encryption for host password
# Test insertResponse()
# Look in meeting.py for getHost and getToken to look about inserting meetings/hosts into the DB
# In host_connect() in main.py, use 'cookie' variable for meeting ID

import sqlite3
import hashlib

from .feedbackClasses import *

class DBController:

    # Establishes DB connection and a cursor
    def __init__(self):
        try:
            self.conn = sqlite3.connect('live_feedback.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print("Failed to open database connection", error)

    def close(self):
        """Closes connection to database
        """
        self.conn.close()

    # Helper function to retrieve common attributes among all feedback types
    def __getGeneralAttributes(self, feedbackObj):
        meeting = feedbackObj.getMeeting()
        anonBool = feedbackObj.getAnon()
        if anonBool == True:
            anon = 1
        else:
            anon = 0
        attendee = feedbackObj.getAttendee()
        return (meeting, anon, attendee)

    # Helper function to insert a general feedback type
    def __insertFeedback(self, meeting, attendee, ftype, anon):
        try:
            self.cursor.execute("INSERT INTO feedback VALUES (NULL, :m, :a, :t, :n)",{'m':meeting, 'a':attendee, 't':ftype, 'n':anon})
            self.cursor.execute("SELECT last_insert_rowid()")
            return self.cursor.fetchone()[0]
        except sqlite3.Error as error:
            return error

    def insertError(self, error):
        """Stores feedback of type: Error

        Parameters:
            error {ErrorFeedback} -- ErrorFeedback object containing details of error

        """
        (meeting, anon, attendee) = self.__getGeneralAttributes(error)
        errType = error.getErrorType()
        errMsg = error.getErrorMessage()

        feedback = self.__insertFeedback(meeting, attendee, "error", anon)

        if type(feedback) is int:
            try:
                self.cursor.execute("INSERT INTO errors VALUES (:f, :t, :m)",{'f':feedback, 't':errType, 'm':errMsg})
                self.conn.commit()
            except sqlite3.Error as err:
                print("Error inserting into table errors:", err)
                self.conn.rollback()
        else:
            print("Error inserting into table feedback:", feedback)
            self.conn.rollback()

    def insertQuestion(self, question):
        """Stores feedback of type: Question

        Parameters:
            question {QuestionFeedback} -- QuestionFeedback object containing details of question

        """
        (meeting, anon, attendee) = self.__getGeneralAttributes(question)
        qstnMsg = question.getQuestionText()

        feedback = self.__insertFeedback(meeting, attendee, "question", anon)

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
    def __insertGeneralMood(self, feedback, moodType, score, time):
        try:
            self.cursor.execute("INSERT INTO moods VALUES (NULL, :f, :t, :s, :l)",{'f':feedback, 't':moodType, 's':score, 'l':time})
            self.cursor.execute("SELECT last_insert_rowid()")
            return self.cursor.fetchone()[0]
        except sqlite3.Error as error:
            return error

    def insertMood(self, mood):
        """Stores feedback of type: Mood

        Parameters:
            mood {emojiMoodObj/textMoodObj} -- Emoji or Text Mood object containing relevant details

        """
        (meeting, anon, attendee) = self.__getGeneralAttributes(mood)
        moodType = mood.getMoodType()
        score = mood.getMoodScore()
        time = mood.getMoodTime()

        if moodType == "text" or moodType == "emoji":
            feedback = self.__insertFeedback(meeting, attendee, "mood", anon)
            if type(feedback) is int:
                moodID = self.__insertGeneralMood(feedback, moodType, score, time)
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

    def __insertGeneralResponse(self, feedback, responseType, prompt):
        try:
            self.cursor.execute("INSERT INTO responses VALUES (NULL, :f, :t, :p)",{'f':feedback, 't':responseType, 'p':prompt})
            self.cursor.execute("SELECT last_insert_rowid()")
            return self.cursor.fetchone()[0]
        except sqlite3.Error as error:
            return error

    def insertResponse(self, response):
        """Stores feedback of type: Response

        Parameters:
            response {emojiResponseObj/multChoiceResponseObj/testResponseObj} -- Emoji, Multiple Choice, or Text Response object containing relevant details

        """
        (meeting, anon, attendee) = self.__getGeneralAttributes(response)
        responseType = response.getResponseType()
        prompt = response.getResponsePrompt()

        if responseType == "emoji" or responseType == "text" or responseType == "multchoice":
            feedback = self.__insertFeedback(meeting, attendee, "response", anon)
            if type(feedback) is int:
                responseID = self.__insertGeneralResponse(feedback, responseType, prompt)
                if type(responseID) is int:
                    if responseType == "emoji":
                        emojiType = response.getResponseEmoji()
                        try:
                            self.cursor.execute("INSERT INTO emoji_responses VALUES (:r, :t)",{'r':responseID, 't':emojiType})
                            self.conn.commit()
                        except sqlite3.Error as error:
                            print("Error inserting into table emoji_responses:",error)
                            self.conn.rollback()
                    elif responseType == "text":
                        message = response.getResponseText()
                        try:
                            self.cursor.execute("INSERT INTO text_responses VALUES (:r, :m)",{'r':responseID, 'm':message})
                            self.conn.commit()
                        except sqlite3.Error as error:
                            print("Error inserting into table text_responses:",error)
                            self.conn.rollback()
                    else:
                        choice = response.getResponseChoice()
                        try:
                            self.cursor.execute("INSERT INTO mult_choice_responses VALUES (:r, :c)",{'r':responseID, 'c':choice})
                            self.conn.commit()
                        except sqlite3.Error as error:
                            print("Error inserting into table mult_choice_responses:",error)
                            self.conn.rollback()
                else:
                    print("Error inserting into table responses:", responseID)
                    self.conn.rollback()
            else:
                print("Error inserting into table feedback:", feedback)
        else:
            print("Invalid response type:", responseType)


    def createEvent(self, host, title):
        """Store event

        Parameters:
            host {int} -- Identifier for host
            title {string} -- Title of the event

        Returns:
            event {int} -- Identifier of created event

        """
        table = "hosts"
        event = -1
        try:
            self.cursor.execute("SELECT hostid FROM hosts WHERE hostid = :h",{'h':host})
            if not self.cursor.fetchone():
               self.cursor.execute("INSERT INTO hosts VALUES (:h)",{'h':host})
            table = "meetings"
            self.cursor.execute("INSERT INTO meetings VALUES (NULL, :h, :t, :r)",{'h':host, 't':title, 'r':121})
            self.cursor.execute("SELECT last_insert_rowid()")
            event = self.cursor.fetchone()[0]
            self.conn.commit()
        except sqlite3.Error as error:
            print("Error inserting into table",table,":",error)
            self.conn.rollback()
        finally:
            return event

    def addAttendee(self, attendee, meeting):
        """Store attendee in specified event

        Parameters:
            attendee {int} -- Identifier for attendee
            meeting {int} -- Identifier for event

        """
        try:
            self.cursor.execute("INSERT INTO attendees VALUES (:a, :m)",{'a':attendee, 'm':meeting})
            self.conn.commit()
        except sqlite3.Error as error:
            print("Error inserting into table attendees:",error)