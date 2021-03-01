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
            if (this.questions[i].type === "multichoice") {
                for (var j = 0; j < this.questions[i].choice_list.length; j++) {
                    outString += `<p>` + this.questions[i].choice_list[j] + `</p>`
                }
            }
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
        
        var newQuestions = data["questions"];
        var newQuestion;

        for(var i = 0; i < newQuestions.length; i++) {
            newQuestion = new Question(newQuestions[i]["type"]);
            newQuestion.setQuestion(newQuestions[i]["question"]);
            this.questions.push(newQuestion)
        }
    }
}