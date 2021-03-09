var searchResults = new SearchResults();
var meetingInfo;

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
        meetingInfo = new MeetingInfo(data);
        document.getElementById("search").style = "display:none";
        meetingInfo.display(document.getElementById("info"));
    });
}