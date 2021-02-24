class QuestionTemplate{
    constructor() {
        this.questions = [];
    }

    addQuestion(question) {
        this.questions.push(question);
    }

    getDisplayString() {
        var outString = "";
        for (var i = 0; i < this.questions.length; i++) {
            outString += `<p>` + this.questions[i].question + `</p>`
        }
        return outString;
    }

    displayTemplate(node) {
        node.innerHTML = this.getDisplayString();
    }

    getJSONString() {
        var JSONString = `{"questions":[`;

        for (var i = 0; i < this.questions.length; i++) {
            JSONString += this.questions[i].getJSONString() + ",";
        }

        JSONString = JSONString.substring(0, JSONString.length - 1) + "]}";
        return JSONString;
    }

    fromJSON(data) {
        this.questions = [];

        var newQuestion;

        for(var i = 0; i < data.length; i++) {
            newQuestion = new Question(data[i]["type"]);
            newQuestion.setQuestion(data[i]["question"]);
            this.questions.push(newQuestion)
        }
    }
}