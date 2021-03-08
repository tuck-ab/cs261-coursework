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
            } else {
                var choices = this.template.questions[i].choice_list
                for (var j = 0; j < choices.length; j++) {
                    console.log(choices[j]);
                    loopString += `<input type="button" onclick="sendMultChoiceAns(` + i.toString() + `,` + j.toString() + `)" value=` + choices[j] + `><br>`;
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