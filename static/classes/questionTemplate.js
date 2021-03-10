class QuestionTemplate{
    constructor() {
        this.questions = [];
    }

    addQuestion(question) {
        this.questions.push(question);
    }

    // Generates a string of HTML which represents the information
    getDisplayString() {
        var outString = "";
        for (var i = 0; i < this.questions.length; i++) {
            outString += `<p>` + this.questions[i].question + `</p>`

            if (this.questions[i].type === "multichoice") {
                for (var j = 0; j < this.questions[i].choice_list.length; j++) {
                    outString += `<p>  - ` + this.questions[i].choice_list[j] + `</p>`
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

        if (this.questions.length > 0) {
            JSONString = JSONString.substring(0, JSONString.length - 1)
        }
        
        JSONString += "]}";
        return JSONString;
    }

    fromJSON(data) {
        this.questions = [];
        
        var newQuestions = data["questions"];
        var newQuestion;

        for (var i = 0; i < newQuestions.length; i++) {
            newQuestion = new Question(newQuestions[i]["type"]);
            //console.log(newQuestions[i]["type"]);
            newQuestion.setQuestion(newQuestions[i]["question"]);
            // If the question is multiple choice, add the multiple choices to the 
            // choice_list array of the multiple choice question!
            var options = newQuestions[i]["options"];
            if (newQuestion.type === "multichoice") {
                for (var j = 0; j < options.length; j++) {
                    newQuestion.choice_list.push(options[j]);
                }
            }

            this.questions.push(newQuestion)
        }

    }
    
}