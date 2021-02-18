from classes import *

test1 = EmojiMood(False,1011,0,1)
test2 = EmojiResponse(True,1111,"this is the prompt",2)
test3 = ErrorFeedback(True,1234,"Audio","We cant hear you")
test4 = GeneralFeedback(False,3333)
test5 = Mood(False, 4311, 0.6)
test6 = MultChoiceResponse(True, 9377, "this is my prompt", 3)
test7 = Question(False, 5372, "is this a question?")
test8 = Response(True, 3336,"this is another response")
test9 = TextMood(True, 1001, 0.7, "this is the text")
test10 = TextResponse(False, 8559,"This is another prompt","this is response")
test11 = EmojiPrompt(3111, "This is the host prompt",[1,2,3,4])
test12 = GeneralPrompt(4422, "prompt prompt prompt")
test13 = MultChoicePrompt(5532, "prrrromppt",["a","b","c","d"])





print(test1.getMoodEmoji())
print(test2.getAttendee())
print(test3.getErrorMessage())
print(test4.getAnon())
print(test5.getMoodScore())
print(test6.getResponsePrompt())
print(test7.getQuestionText())
print(test8.getResponsePrompt())
print(test9.getMoodText())
print(test10.getResponsePrompt())
print(test11.getHost())
print(test12.getPromptText())
print(test13.getMultChoices())