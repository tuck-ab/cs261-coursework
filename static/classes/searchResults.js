class SearchResults {
    constructor() {
        this.results = [];
        this.filtered_results = [];
    }

    setResults(results, search) {
        this.results = results;
        this.setFilteredResults(search);
    }
    
    setFilteredResults(keyword) {
        keyword = keyword.toLowerCase()
        this.filtered_results = [];

        for (var i = 0; i < this.results.length; i++) {
            if (this.results[i]["title"].toLowerCase().includes(keyword)) {
                this.filtered_results.push(this.results[i])
            }
        }
    }

    getResultString(id) {
        return `{"meetingid":"` + this.filtered_results[id]["meeting_id"] + `"}`;
    }

    // Generates a string of HTML which represents the information
    getHTMLString() {
        var HTMLString = "";
        var loopString = "";

        for (var i = 0; i < this.filtered_results.length; i++) {
            loopString = `<div class="searchResult" onclick="selectResult(` + i.toString() + `)">`
            loopString += `<p>Title: ` + this.filtered_results[i]["title"] + `</p>`;
            loopString += `<p>Start Time: ` + this.filtered_results[i]["date_time"] + `</p>`;
            loopString += `<p>Duration: ` + this.filtered_results[i]["run_time"] + `</p>`;
            loopString += `</div>`

            HTMLString += loopString;
        }

        return HTMLString;
    }

    display(node) {
        node.innerHTML = this.getHTMLString();
    }
}