# TODO:
# Create encryption for meeting password
# In host_connect() in main.py, use 'cookie' variable for meeting ID

import hashlib
import secrets
import sqlite3
import string
import time

from .feedbackClasses import *

class DBController:

    def __init__(self):
        # Establishes DB connection and a cursor
        try:
            self.conn = sqlite3.connect('live_feedback.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print("Failed to open database connection", error)

    def close(self):
        """Closes connection to database
        """
        self.conn.close()

    def __insert_feedback(self, meeting, f_type):
        # Helper function to insert a general feedback type
        try:
            self.cursor.execute("INSERT INTO feedback VALUES (NULL, :m, :t)",{'m':meeting, 't':f_type})
            self.cursor.execute("SELECT last_insert_rowid()")
            return self.cursor.fetchone()[0]
        except sqlite3.Error as error:
            return error

    def insert_error(self, error):
        """Stores feedback of type: Error

        Parameters:
            error {ErrorFeedback} -- ErrorFeedback object containing details of error

        """
        meeting = error.getMeeting()
        err_type = error.getErrorType()
        err_msg = error.getErrorMessage()

        feedback = self.__insert_feedback(meeting, "error")

        if type(feedback) is int:
            try:
                self.cursor.execute("INSERT INTO errors VALUES (:f, :t, :m)",{'f':feedback, 't':err_type, 'm':err_msg})
                self.conn.commit()
            except sqlite3.Error as err:
                print("Error inserting into table errors:", err)
                self.conn.rollback()
        else:
            print("Error inserting into table feedback:", feedback)
            self.conn.rollback()

    def insert_question(self, question):
        """Stores feedback of type: Question

        Parameters:
            question {QuestionFeedback} -- QuestionFeedback object containing details of question

        """
        meeting = question.getMeeting()
        qstn_msg = question.getQuestionText()

        feedback = self.__insert_feedback(meeting, "question")

        if type(feedback) is int:
            try:
                self.cursor.execute("INSERT INTO questions VALUES (:f, :m)",{'f':feedback, 'm':qstn_msg})
                self.conn.commit()
            except sqlite3.Error as error:
                print("Error inserting into table questions:", error)
                self.conn.rollback()
        else:
            print("Error inserting into table feedback:", feedback)
            self.conn.rollback()

    def __insert_general_mood(self, feedback, mood_type, score, time):
        # Helper function to insert a general mood feedback
        try:
            self.cursor.execute("INSERT INTO moods VALUES (NULL, :f, :t, :s, :l)",{'f':feedback, 't':mood_type, 's':score, 'l':time})
            self.cursor.execute("SELECT last_insert_rowid()")
            return self.cursor.fetchone()[0]
        except sqlite3.Error as error:
            return error

    def insert_mood(self, mood):
        """Stores feedback of type: Mood

        Parameters:
            mood {emojiMoodObj/textMoodObj} -- Emoji or Text Mood object containing relevant details

        """
        meeting = mood.getMeeting()
        mood_type = mood.getMoodType()
        score = mood.getMoodScore()
        time = round(mood.getMoodTime()/60)

        if mood_type == "text" or mood_type == "emoji":
            feedback = self.__insert_feedback(meeting, "mood")
            if type(feedback) is int:
                mood_ID = self.__insert_general_mood(feedback, mood_type, score, time)
                if type(mood_ID) is int:
                    if mood_type == "text":
                        data = mood.getMoodText()
                    else:
                        data = mood.getMoodEmoji()
                    try:
                        self.cursor.execute("INSERT INTO " + mood_type + "_moods VALUES (:m, :t)",{'m':mood_ID, 't':data})
                        self.conn.commit()
                    except sqlite3.Error as error:
                        print("Error inserting into table " + mood_type + "_moods:", error)
                        self.conn.rollback()
                else:
                    print("Error inserting into table moods:", mood_ID)
                    self.conn.rollback()
            else:
                print("Error inserting into table feedback:", feedback)
                self.conn.rollback()
        else:
            print("Invalid mood type:", mood_type)

    def __insert_general_response(self, feedback, response_type, prompt):
        # Helper function to insert a general response feedback
        try:
            self.cursor.execute("INSERT INTO responses VALUES (NULL, :f, :t, :p)",{'f':feedback, 't':response_type, 'p':prompt})
            self.cursor.execute("SELECT last_insert_rowid()")
            return self.cursor.fetchone()[0]
        except sqlite3.Error as error:
            return error

    def insert_response(self, response):
        """Stores feedback of type: Response

        Parameters:
            response {emojiResponseObj/multChoiceResponseObj/testResponseObj} -- Emoji, Multiple Choice, or Text Response object containing relevant details

        """
        meeting = response.getMeeting()
        response_type = response.getResponseType()
        prompt = response.getResponsePrompt()['question']

        if response_type == "emoji" or response_type == "text" or response_type == "multchoice":
            feedback = self.__insert_feedback(meeting, "response")
            if type(feedback) is int:
                response_ID = self.__insert_general_response(feedback, response_type, prompt)
                if type(response_ID) is int:
                    if response_type == "emoji":
                        data = response.getResponseEmoji()
                    elif response_type == "text":
                        data = response.getResponseText()
                    else:
                        data = response.getResponseChoice()
                        response_type = "mult_choice"
                    try:
                        self.cursor.execute("INSERT INTO " + response_type + "_responses VALUES (:r, :d)",{'r':response_ID, 'd':data})
                        self.conn.commit()
                    except sqlite3.Error as error:
                        print("Error inserting into table " + response_type +"_responses:", error)
                        self.conn.rollback()
                else:
                    print("Error inserting into table responses:", response_ID)
                    self.conn.rollback()
            else:
                print("Error inserting into table feedback:", feedback)
                self.conn.rollback()
        else:
            print("Invalid response type:", response_type)

    def uniqueToken(self, token):
        """Determines if token is unique

        Parameters:
            token {int} -- Token to check uniqueness of

        Returns:
            True/False {boolean} -- Indicates whether token is unique
        """
        try:
            self.cursor.execute("SELECT meetingid FROM meetings WHERE meetingid == :m",{'m':token})
            if self.cursor.fetchone() is None:
                return True
            return False
        except sqlite3.Error as error:
            print("Error selecting meetingid from table meetings:",error)
            return False

    def insert_meeting(self, token, details):
        """Stores newly created meeting

        Parameters:
            token {int} -- Identifier for the given meeting
            details {dict} -- Stores meeting title in key 'name' and meeting password in key 'keyword'
        """
        title = details['name']
        password = details['keyword']
        alphabet = string.ascii_letters + string.digits
        salt = hashlib.sha256(''.join(secrets.choice(alphabet) for i in range(8)).encode('utf-8')).hexdigest()
        meeting_pass = hashlib.sha256((password + "--" + salt).encode('utf-8')).hexdigest()
        t = time.time()
        date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
        try:
            self.cursor.execute("INSERT INTO meetings VALUES (:m, :t, :p, :s, 0, :d)",{'m':token, 't':title, 'p':meeting_pass, 's':salt, 'd':date_time})
            self.conn.commit()
        except sqlite3.Error as error:
            print("Error inserting into table meetings:",error)
            self.conn.rollback()

    # Searches for all meetings with a certain string in their title
    def search_meetings(self,query):
        try:
            self.cursor.execute("SELECT title, date_time FROM meetings WHERE title LIKE '%?%'",(query,))
            matches = self.cursor.fetchall()
            return matches

        except sqlite3.Error as error:
            return error

    # def __checkCred(self, sockid, password):
    #     try:
    #         self.cursor.execute("SELECT hostid, hostpass, salt FROM hosts WHERE socketid = :s",{'s':sockid})
    #         fetched = self.cursor.fetchone()
    #         hostpass = fetched[1]
    #         salt = fetched[2]
    #         if hashlib.sha1(password + "--" + salt) == hostpass:
    #             return fetched[0]
    #         else:
    #             return "Incorrect credentials"
    #     except sqlite3.Error as error:
    #         return error
