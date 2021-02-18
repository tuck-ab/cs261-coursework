class Question {
    constructor(type) {
        this.type = type;
        this.question = "";
    }

    setQuestion(question) {
        this.question = question;
    }

    getJSONString() {
        return `{"question":"` + this.question + `", "type":"` + this.type + `"}`;
    }
}