class MultChoiceCreate {
    constructor() {
        this.options = ["",""]
    }

    // Generates a string of HTML which represents the information
    getHTMLString() {
        var HTMLString = "";
        var loopString = "";

        for (var i = 0; i < this.options.length; i++) {
            loopString = `<input type="text" id="option` + i.toString() + `" `;
            loopString += `value="` + this.options[i] + `" `;
            loopString += `onchange="updateOption(` + i.toString() + `)">`

            loopString += `<input type="button" onclick="removeOption(` + i.toString() + `)" `;
            loopString +=  `value="Remove">`;

            loopString += `<br>`;

            HTMLString += loopString;
        }

        return HTMLString;
    }

    display(node) {
        node.innerHTML = this.getHTMLString()
    }

    addOption() {
        this.options.push("")
    }

    updateOption(num, val) {
        this.options[num] = val;
    }

    removeOption(num) {
        if (this.options.length > 2) {
            this.options.splice(num, 1);
        }
    }
}
