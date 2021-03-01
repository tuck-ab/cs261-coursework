class Question {

    constructor(type) {
        // Types can be : "normal" for open-ended questions or "multchoice" for multiple-choice questions
        this.type = type;
        this.question = "";
        // If the question is of type "multchoice" then the multiple choices are added to this list below
        this.choice_list = [];
    }

    setQuestion(question) {
        this.question = question;
    }

    addChoice(choice) {
        this.choice_list.push(choice);
    }

    getJSONString() {
        if (this.type === "multichoice") {
            var choices = this.choice_list[0]
            for (var i = 1; i < this.choice_list.length; i++) {
                choices += " , "
                choices += this.choice_list[i]
            }
            return `{"question":"` + this.question + `", "type":"` + this.type + `", "choices":"` + choices + `"}`;
        }
        else {
            return `{"question":"` + this.question + `", "type":"` + this.type + `"}`;
        }
    }

    getAsJSON() {
        if (this.type === "multichoice") {
            var choices = this.choice_list[0]
            for (var i = 1; i < this.choice_list.length; i++) {
                choices += " , "
                choices += this.choice_list[i]
            }
            return { "question": this.question, "type": this.type, "choices": choices };
        }
        else {
            return { "question": this.question, "type": this.type }; 
        }
    }


}