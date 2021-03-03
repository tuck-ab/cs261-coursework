var searchResults = new SearchResults();

function searchUpdate() {
    $.ajax({
        data : {
        query : document.getElementById("meetingSearch").value
            },
        type : 'POST',
        url : '/meeting_search'
        })
    .done(function(data) {
        searchResults.setResults(data["results"]);
        searchResults.display(document.getElementById("results"));
    });
    event.preventDefault();
}

function selectResult(id) {
    console.log(id);
}