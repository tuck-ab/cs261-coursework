class QuestionTemplate{
    constructor() {
        this.questions = [];
    }

    addQuestion(question) {
        this.questions.push(question);
    }

    getDisplayString() {
        var outString = "";
        for (i = 0; i < this.questions.length; i++) {
            outString += `<p>` + this.questions[i].question + `</p>`
        }
    }

    displayTemplate(node) {
        node.innerHTML = this.getDisplayString();
    }

    getJSONString() {
        var JSONString = `{"questions":[`;

        for (i = 0; i < this.questions; i++) {
            JSONString += this.questions[i].getJSONString() + ",";
        }

        JSONString = JSONString.substring(0, JSONString.length - 1) + "]}";
        return JSONString;
    }
}