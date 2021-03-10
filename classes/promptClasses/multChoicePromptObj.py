from .generalPromptObj import GeneralPrompt

class MultChoicePrompt(GeneralPrompt):

    def __init__(self, host_id, meeting_id, prompt_text, mult_choices = list()):
        super().__init__(host_id, meeting_id, prompt_text)
        self.mult_choices = mult_choices
    
    def get_mult_choices(self):
        return self.mult_choices

    def add_choice(self,choice):
        self.mult_choices.append(choice)
    
    def remove_choice(self,choice):
        self.mult_choices.remove(choice)
        
