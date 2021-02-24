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
}