class Question {
    constructor(type) {
        // Types can be: "normal"
        this.type = type;
        this.question = "";
    }

    setQuestion(question) {
        this.question = question;
    }

    getJSONString() {
        if (this.type === "normal") {
            return `{"question":"` + this.question + `", "type":"` + this.type + `"}`;
        }
    }

    getAsJSON() {
        if (this.type === "normal") {
            return {"question":this.question, "type":this.type};
        }
    }
}