class Template:
    def __init__(self):
        self.questions = []

    def fromJSON(self, json_dict):
        """Maps the JSON dictionary given to the correct format for this object

        The current JSON format used is:
            {"questions": [{"question": "", "type":""}, ... , {"question": "", "type":""}]}

        """

        questions = json_dict["questions"]
        self.questions = []

        for question in questions:
            self.questions.append(Question(question["type"]))
            self.questions[-1].set_question(question["question"])

        return self

    def getJSON(self):
        """
        Returns a python dictionary to be used to send the template in a JSON format 
        """

        json_dict = {"questions": []}
        for item in self.questions:
            json_dict["questions"].append(item.get_json())

        return json_dict

    def __str__(self):
        return str(self.getJSON())

class Question:
    def __init__(self, q_type):
        self.type = q_type
        self.question = ""

    def set_question(self, question):
        self.question = question

    def get_json(self):
        return {"question":self.question, "type": self.type}