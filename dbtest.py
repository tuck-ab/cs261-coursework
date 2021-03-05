import time

from classes import *

connection = DBController()

print(connection.add_new_host("michael", "notacult")) # returns None since user 'michael' already exists
print(connection.add_new_host("torsten", "deduction")) # returns a token since 'torsten' is a new user 

print(connection.unique_token(2222)) # returns False, since meeting ID 2222 exists
print(connection.unique_token(5555)) # returns True, since 5555 is a non-existing meeting ID

connection.insert_meeting(5555, 5, "Logic and Verification") # inserts new meeting

test_error = ErrorFeedback(True,1,5555,"video","Whiteboard out of focus")
connection.insert_error(test_error) # inserts error

test_question = QuestionFeedback(False,2,5555,"When can I use Modus Ponens?")
connection.insert_question(test_question) # inserts question

test_text_mood = TextMood(True,4,5555,"text",0.5,time.time(),1,"Great work!")
connection.insert_mood(test_text_mood) # inserts text mood

test_emoji_mood = EmojiMood(False,3,5555,"emoji",-0.8,time.time(),1,":confused:")
connection.insert_mood(test_emoji_mood) # inserts emoji mood

test_emoji_response = EmojiResponse(False,3,5555,"emoji","What is the symbol for implication?",":arrow_right:")
connection.insert_response(test_emoji_response) # inserts emoji response

test_text_response = TextResponse(True,1,5555,"text","What is DNF?","A disjunction of conjunctions")
connection.insert_response(test_text_response) # inserts text response

test_mult_response = MultChoiceResponse(False,2,5555,"multchoice","True of False? 3-SAT can be reduced to 2-SAT","False")
connection.insert_response(test_mult_response) # inserts multiple choice response

connection.update_runtime(5555) # updates the length of the meeting with ID 5555

print(connection.check_host("torsten", "tableaux")) # returns False; incorrect password
print(connection.check_host("torsten", "deduction")) # returns True; correct password

connection.close()