from classes import *

connection = DBController()

testError = ErrorFeedback(True,1,1,"Test","Just testing the feedback!")
connection.insertError(testError)

testQuestion = QuestionFeedback(False,2,3,"What is a rational agent?")
connection.insertQuestion(testQuestion)

connection.close()