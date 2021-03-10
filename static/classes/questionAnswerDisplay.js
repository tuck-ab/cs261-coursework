class QuestionAnswerDisplay{
    constructor() {
        this.questionAnswerList = []
    }

    addQuestionAnswerPair(question, answer) {
        this.questionAnswerList.push({"question":question, "answer":answer});
        if (this.questionAnswerList.length > 5) {
            this.questionAnswerList.splice(0,1);
        }
    }

    // Generates a string of HTML which represents the information
    getHTMLString() {
        var HTMLString = "";

        for (var i = 0; i < this.questionAnswerList.length; i++) {
            HTMLString += `<p>Question: ` + this.questionAnswerList[i]["question"] + `</p>`;
            HTMLString += `<p>Answer: ` + this.questionAnswerList[i]["answer"] + `</p>`;
        }

        return HTMLString;
    }

    displayQuestionAnswer(node) {
        console.log(this.getHTMLString())
        node.innerHTML = this.getHTMLString();
    }
}