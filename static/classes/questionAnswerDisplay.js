class QuestionAnswerDisplay{
    constructor() {
        this.questionAnswerList = []
    }

    addQuestionAnswerPair(question, answer) {
        this.questioinAnswerList.push({"question":question, "answer":answer});
    }

    getHTMLString() {
        var HTMLString = "";

        for (var i = 0; i < this.questionAnswerList; i++) {
            HTMLString += `<p>Question: ` + this.questionAnswerList[i]["question"] + `</p>`;
            HTMLString += `<p>Answer: ` + this.questionAnswerList[i]["answer"] + `</p>`;
        }

        return HTMLString;
    }

    displayQuestionAnswer(node) {
        node.innerHTML = this.getHTMLString();
    }
}