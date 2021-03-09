class MultChoiceQuestionDisplay {
    constructor() {
        this.questions = []
    }

    getHTMLString() {
        var HTMLString = "";
        
        for (var i = 0; i < this.questions.length; i++) {
            HTMLString += `<p>` + this.questions[i]["question"] + `</p><div id="multquestion` + i.toString() + `"></div><br>`
        }
        return HTMLString;
    }

    display(node) {
        node.innerHTML = this.getHTMLString();
        var data;

        for (var i = 0; i < this.questions.length; i++) {
            data = [{
                x: this.getOptions(i),
                y: this.getFrequencies(i),
                type: "bar"
            }];
            console.log("plotting");
            console.log("data");
            Plotly.newPlot("multquestion" + i.toString(), data)
        }
    }

    getOptions(id) {
        var outList = [];
        var optionsList = this.questions[id]["results"]
        console.log("optionslist:")
        console.log(optionsList)
        for (var i = 0; i < optionsList.length; i++) {
            outList.push(optionsList[i][0]);
        }
        console.log(outList)
        return outList
    }

    getFrequencies(id) {
        var outList = [];
        var optionsList = this.questions[id]["results"]
        for (var i = 0; i < optionsList.length; i++) {
            outList.push(optionsList[i][1]);
        }
        console.log(outList)
        return outList
    }

    updateQuestion(data) {
        for (var i = 0; i < this.questions.length; i++) {
            if (this.questions[i]["question"] == data["question"]) {
                this.questions[i]["results"] = data["results"];
                return;
            }
        }
        this.questions.push(data)
    }
}