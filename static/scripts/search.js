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
    var keywordEntered = prompt("Key word:");

    if (keywordEntered !== null) {
        $.ajax({
            data : {
            meeting : searchResults.getResultString(id),
            keyword : keywordEntered
                },
            type : 'POST',
            url : '/meeting_submit'
            })
        .done(function(data) {
            console.log(data);
        });
        event.preventDefault();
    }
}