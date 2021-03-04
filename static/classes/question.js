class Question {
    constructor(type) {
        // Types can be: "normal"
        this.type = type;
        this.question = "";
        // If the question is "multchoice" then the multiple choices are added 
        // to this list below. Note that all multiple choice questions must have 4 choices
        this.choice_list = ["", "", "", ""];
    }

    setQuestion(question) {
        this.question = question;
    }

    getJSONString() {
        if (this.type === "normal") {
            return `{"question":"` + this.question + `", "type":"` + this.type + `"}`;
        }
        else {
            // JSON String simply returns all the different multiple choices. 
            return `{"question":"` + this.question + `", "type":"` + this.type + `", "choice 1":"` + this.choice_list[0] + `", "choice 2":"` + this.choice_list[1] + `", "choice 3":"` + this.choice_list[2] + `", "choice 4":"` + this.choice_list[3] + `"}`;
        }
    }

    getAsJSON() {
        if (this.type === "normal") {
            return {"question":this.question, "type":this.type};
        }
        else {
            return { "question": this.question, "type": this.type, "choice 1": this.choice_list[0], "choice 2": this.choice_list[1], "choice 3": this.choice_list[2], "choice 4": this.choice_list[3] };
        }
    }
}