function searchUpdate() {
    $.ajax({
        data : {
        query : document.getElementById("meetingSearch").value
            },
        type : 'POST',
        url : '/meeting_search'
        })
    .done(function(data) {
        console.log(data);
    });
    event.preventDefault();
}