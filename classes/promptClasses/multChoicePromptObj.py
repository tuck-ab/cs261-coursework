import generalPromptObj

class MultChoicePrompt(generalPromptObj.GeneralPrompt):

    def __init__(self, hostID, promptText, multChoices = list()):
        super().__init__(hostID, promptText)
        self.multChoices = multChoices
    
    def getMultChoices(self):
        return self.multChoices

    def addChoice(self,choice):
        self.multChoices.append(choice)
    
    def removeChoice(self,choice):
        self.multChoices.remove(choice)


testList = ["choice1","choice2","choice3","choice5"]
test = MultChoicePrompt(1010101, "this is the text", testList)

print(test.getMultChoices())
test.addChoice("choice4")
print(test.getMultChoices())
test.removeChoice("choice5")
print(test.getMultChoices())
