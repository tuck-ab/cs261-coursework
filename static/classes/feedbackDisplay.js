class FeedbackDisplay {
    constructor() {
        this.feedbackList = [];
    }

    addFeedback(feedback) {
        this.feedbackList.push(feedback);
        if (this.feedbackList.length > 5) {
            this.feedbackList.splice(0,1);
        }
    }

    // Generates a string of HTML which represents the information
    getHTMLString() {
        var HTMLString = "";
        
        for (var i = 0; i < this.feedbackList.length; i++) {
            HTMLString += `<p>` + this.feedbackList[i] + `</p>`
        }

        return HTMLString;
    }

    displayFeedback(node) {
        node.innerHTML = this.getHTMLString();
    }
}