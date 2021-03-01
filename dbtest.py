from classes import *

connection = DBController()

# connection.createEvent(3, "Software Engineering")
# connection.createEvent(4, "Formal Languages")

# connection.addAttendee(5,3)

# testError = ErrorFeedback(True,1,1,"Test","Just testing the feedback!")
# connection.insertError(testError)

# testQuestion = QuestionFeedback(False,2,3,"What is a rational agent?")
# connection.insertQuestion(testQuestion)

# testTextMood = TextMood(True,4,2,"text",0.5,"Pretty good")
# connection.insertMood(testTextMood)

# testEmojiMood = EmojiMood(False,3,4,"emoji",-0.8,":confused:") # int or string?
# connection.insertMood(testEmojiMood)

# testEmojiResponse = EmojiResponse(False, 3, 2, "emoji", "If two processes are waiting for one another to terminate, it is called a dead___",":lock:")
# connection.insertResponse(testEmojiResponse)

# testTextResponse = TextResponse(True, 1, 1, "text", "What programming paradigm does Haskell use?", "Functional paradigm")
# connection.insertResponse(testTextResponse)

# testMultResponse = MultChoiceResponse(False, 2, 4, "multchoice", "True of False? Kruskal's algorithm is a greedy algorithm", "True")
# connection.insertResponse(testMultResponse)

connection.close()