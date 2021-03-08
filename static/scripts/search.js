var searchResults = new SearchResults();

function getMeetings() {
    $.ajax({
        data : {
            },
        type : 'POST',
        url : '/meeting_search'
        })
    .done(function(data) {
        searchResults.setResults(data["results"], document.getElementById("meetingSearch").value);
        searchResults.display(document.getElementById("results"));
    });
}

getMeetings();

function searchUpdate() {
    searchResults.setFilteredResults(document.getElementById("meetingSearch").value);
    searchResults.display(document.getElementById("results"));
}

function selectResult(id) {
    $.ajax({
        data : {
        meeting : searchResults.getResultString(id)
            },
        type : 'POST',
        url : '/meeting_submit'
        })
    .done(function(data) {
        console.log(data);
    });
}