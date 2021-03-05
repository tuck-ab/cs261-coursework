var searchResults = new SearchResults();

function getMeetings() {
    $.ajax({
        data : {
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

getMeetings();

function searchUpdate() {
    
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