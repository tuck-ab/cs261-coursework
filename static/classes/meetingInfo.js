class MeetingInfo {
    constructor(info) {
        this.errors = info["errors"];
        this.questions = info["question"];
        this.multChoiceQuestions = info["mult_choice"];
        this.finalMood = info["final_mood"];
        this.averageMood = info["average_mood"];
    }

    // Generates a string of HTML which represents the information
    getHTMLString() {
        var HTMLString = "";
        var loopString;

        HTMLString += `<p>Final Mood Score: ` + this.finalMood + `</p>`;
        HTMLString += `<p>Average Mood Score: ` + this.averageMood + `</p>`;

        var answers;
        for (var i = 0; i < this.questions.length; i++) {
            loopString = `<p>Question: ` + this.questions[i][0] + `</p>`
            answers = this.questions[i][1];
            for (var j = 0; j < answers.length; j++) {
                loopString += `<p>` + answers[j] + `</p>`;
            }

            loopString += "<br>";
            HTMLString += loopString;
        }

        for (var i = 0; i < this.multChoiceQuestions.length; i++) {
            loopString = `<p>Question: ` + this.multChoiceQuestions[i][0] + `</p>`;
            loopString += `<div style="width:50%;margin-left:auto;margin-right:auto;" id="multchoice` + i.toString() + `"></div>`;
            HTMLString += loopString;
        }

        HTMLString += `<p>Errors reported during the event:</p>`;
        for (var i = 0; i < this.errors.length; i++) {
            HTMLString += `<p>` + this.errors[i] + `</p>`;
        }

        return HTMLString;
    }

    display(node) {
        node.innerHTML = this.getHTMLString();

        var data;

        for (var i = 0; i < this.multChoiceQuestions.length; i++) {
            data = [{
                x: this.getOptions(i),
                y: this.getValues(i),
                type: "bar"
            }];
            Plotly.newPlot("multchoice" + i.toString(), data)
        }
    }

    getOptions(id) {
        return this.multChoiceQuestions[id][1];
    }

    getValues(id) {
        return this.multChoiceQuestions[id][2];
    }
}