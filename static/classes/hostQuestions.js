class HostQuestions{
    constructor() {
        this.template = new QuestionTemplate();
    }

    fromJSON(data) {
        this.template.fromJSON(data);
    }

    getDisplayString() {
        var outString = "";
        var loopString = "";

        for (var i = 0; i < this.template.questions.length; i++) {
            loopString = `<p>` + this.template.questions[i].question + `</p>`;
            loopString += `<input type="text" id="question_` + i.toString() +`">`;
            loopString += `<input type="button" onclick="sendQuestionAnswer(` + i.toString() + `)" value="Send"><br>`;

            outString += loopString;
        }

        return outString;
    }

    displayTemplate(node) {
        node.innerHTML = this.getDisplayString();
    }
}