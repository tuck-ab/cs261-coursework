class SearchResults {
    constructor() {
        this.results = [];
    }

    setResults(results) {
        this.results = results;
    }

    getResultString(id) {
        return `{"meetingid":"` + this.results[id]["meeting_id"] + `"}`;
    }

    getHTMLString() {
        var HTMLString = "";
        var loopString = "";

        for (var i = 0; i < this.results.length; i++) {
            loopString = `<div class="searchResult" onclick="selectResult(` + i.toString() + `)">`
            loopString += `<p>Title: ` + this.results[i]["title"] + `</p>`;
            loopString += `<p>Start Time: ` + this.results[i]["date_time"] + `</p>`;
            loopString += `<p>Duration: ` + this.results[i]["run_time"] + `</p>`;
            loopString += `</div>`

            HTMLString += loopString;
        }

        return HTMLString;
    }

    display(node) {
        node.innerHTML = this.getHTMLString();
    }
}