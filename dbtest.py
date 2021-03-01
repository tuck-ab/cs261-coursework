from classes import *

connection = DBController()

test_error = ErrorFeedback(True,1,1,"Test","Just testing the feedback!")
connection.insert_error(test_error)

test_question = QuestionFeedback(False,2,3,"What is a rational agent?")
connection.insert_question(test_question)

test_text_mood = TextMood(True,4,2,"text",0.5,600,"Pretty good")
connection.insert_mood(test_text_mood)

test_emoji_mood = EmojiMood(False,3,4,"emoji",-0.8,660,":confused:")
connection.insert_mood(test_emoji_mood)

test_emoji_response = EmojiResponse(False, 3, 2, "emoji", "If two processes are waiting for one another to terminate, it is called a dead___",":lock:")
connection.insert_response(test_emoji_response)

test_text_response = TextResponse(True, 1, 1, "text", "What programming paradigm does Haskell use?", "Functional paradigm")
connection.insert_response(test_text_response)

test_mult_response = MultChoiceResponse(False, 2, 4, "multchoice", "True of False? Kruskal's algorithm is a greedy algorithm", "True")
connection.insert_response(test_mult_response)

connection.close()