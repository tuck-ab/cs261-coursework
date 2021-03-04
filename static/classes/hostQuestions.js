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
            if (this.template.questions[i].type === "normal") {
                loopString += `<input type="text" id="question_` + i.toString() + `">`;
            }
            else {
                for (var j = 0; j < 4; j++) {
                    console.log(this.template.questions[i].choice_list[j]);
                    loopString += `<input type="button" onclick="updateQuestionAnswer(` + i.toString() + `,` + j.toString() + `)" value=` + this.template.questions[i].choice_list[j] + `><br>`;
                }
            }
            loopString += `<input type="button" onclick="sendQuestionAnswer(` + i.toString() + `)" value="Send"><br>`;


            outString += loopString;
        }

        return outString;
    }

    displayTemplate(node) {
        node.innerHTML = this.getDisplayString();
    }
}