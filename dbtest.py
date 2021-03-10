import time

from classes import *

connection = DBController()

conn = sqlite3.connect('live_feedback.db')
c = conn.cursor()

schema = open("database/schema.sql")
schema_string = schema.read()
c.executescript(schema_string)

schema = open("database/data.sql")
schema_string = schema.read()
c.executescript(schema_string)

assert(connection.add_new_host("michael", "notacult") is None) # User 'michael' already exists
token = connection.add_new_host("torsten", "deduction")
assert(token is not None) # User 'torsten' is new
assert(connection.check_token(token)) # Valid token returned

assert(not connection.unique_token(2222)) # Meeting ID 2222 exists
assert(connection.unique_token(5555)) # Meeting ID 5555 is new

connection.insert_meeting(5555, token, "Logic and Verification") # Insert new meeting

# connection.insert_meeting(5556, token, "Logic and Verification 2")
# connection.insert_meeting(5557, token, "Logic and Verification 3")
# connection.insert_meeting(5558, token, "Logic and Verification 4")

# print(connection.get_meetings(token))

test_error = ErrorFeedback(1,5555,"video","Whiteboard out of focus")
connection.insert_error(test_error) # Insert error

test_question = QuestionFeedback(2,5555,"When can I use Modus Ponens?")
connection.insert_question(test_question) # Insert question

test_text_mood = TextMood(4,5555,"text",0.5,time.time(),1,"Great work!")
connection.insert_mood(test_text_mood) # Insert text mood

test_emoji_mood = EmojiMood(3,5555,"emoji",-1.0,time.time(),1,-1.0)
connection.insert_mood(test_emoji_mood) # Insert emoji mood

test_emoji_response = EmojiResponse(3,5555,"emoji","What is the symbol for implication?",":arrow_right:")
connection.insert_response(test_emoji_response) # Insert emoji response

test_text_response = TextResponse(1,5555,"text","What is DNF?","A disjunction of conjunctions")
connection.insert_response(test_text_response) # Insert text response

test_mult_response = MultChoiceResponse(2,5555,"multchoice","True or False? 3-SAT can be reduced to 2-SAT","False")
connection.insert_response(test_mult_response) # Insert multiple choice response

connection.update_runtime(5555) # Update length of meeting with ID 5555

assert(connection.get_meeting_info(5555,token) ==  {'mult_choice': [['True or False? 3-SAT can be reduced to 2-SAT', ['False'], [1]]], 
                                                    'question': [['What is DNF?', ['A disjunction of conjunctions']]], 
                                                    'final_mood': 0.5, 
                                                    'average_mood': 1.0, 
                                                    'emoji': [1, 0, 0, 0, 0], 
                                                    'errors': ['Whiteboard out of focus'], 
                                                    'general_feedback': [0.5]})

assert(connection.check_host("torsten", "tableaux") is None) # Incorrect password
assert(connection.check_host("torsten", "deduction") is not None) # Correct password

conn.close()

connection.close()

print("All tests passed")