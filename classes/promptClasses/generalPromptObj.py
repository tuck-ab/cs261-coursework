class GeneralPrompt:

    def __init__(self, host_id, meeting_id, prompt_text):
        self.host_id = host_id
        self.prompt_text = prompt_text
        self.meeting_id = meeting_id
    
    def get_host(self):
        return self.host_id

    def get_prompt_text(self):
        return self.prompt_text
    
    def get_meeting(self):
        return self.meeting_id
