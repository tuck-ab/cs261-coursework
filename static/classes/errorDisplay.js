class ErrorDisplay {
    constructor() {
        this.errors = [];
    }

    addError(error) {
        this.errors.push(error)
    }

    getHTMLString() {
        var HTMLString = "";

        for (var i = 0; i < this.errors.length; i++) {
            HTMLString += `<p>` + this.errors[i] + `</p>`;
        }

        return HTMLString
    }

    displayErrors(node) {
        node.innerHTML = this.getHTMLString();
    }
}