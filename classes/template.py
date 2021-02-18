class Template:
    def __init__(self):
        self.questions = []

    def fromJSON(self, json_dict):
        """Uses the JSON string given in the POST request to create a Template object

        The current JSON format used is:
            {"questions": [{"question": ""}, ... , {"question": ""}]}

        """

        questions = json_dict["questions"]

        for question in questions:
            self.questions.append(question["question"])

        return self

    def getJSON(self):
        json_dict = {"questions": []}
        for item in self.questions:
            json_dict["questions"].append({"question": item})

        return json_dict