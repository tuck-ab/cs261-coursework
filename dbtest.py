from classes import *

connection = DBController()
testError = ErrorFeedback(True,1234,"Audio","We cant hear you")

connection.insertError(testError)
connection.close()

# Need to insert host, attendees, and meeting