class ErrorDisplay {
    // Stores all the errors that need to be displayed while also having
    // methods to display the information on the page
    constructor() {
        this.errors = [];
    }

    addError(error) {
        this.errors.push(error)
    }

    removeError(id) {
        this.errors.splice(id, 1);
    }

    // Generates a string of HTML which represents the information
    getHTMLString() {
        var HTMLString = "";

        for (var i = 0; i < this.errors.length; i++) {
            HTMLString += `<p>` + this.errors[i];
            HTMLString += `<input type="button" onclick="removeError(` + i.toString() + `)" value="Remove"></p>`;
        }

        return HTMLString;
    }

    displayErrors(node) {
        node.innerHTML = this.getHTMLString();
    }
}