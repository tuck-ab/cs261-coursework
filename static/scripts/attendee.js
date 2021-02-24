var questionTemplate = new QuestionTemplate();

socket.on("connection_response", function(data) {
    if (data == "connected") {
        socket.emit("connect_as_attendee", {"code" : meetingcode});
    }
});

socket.on("meeting_details", function(data) {
    if (data["connection_status"] == "connected") {
        document.getElementById("connection_status").innerHTML = "Connected to room " + meetingcode.toString();
        
        questionTemplate.fromJSON(data["template"]);
        questionTemplate.displayTemplate(document.getElementById("hostQuestions"));
    } else {
        document.getElementById("connection_status").innerHTML = "Connection failed";
    }
});

socket.on("template_update", function(data) {
    console.log(data);
    questionTemplate.fromJSON(data["template"]);
    questionTemplate.displayTemplate(document.getElementById("hostQuestions"));
});

function sendGeneralFeedback() {
    socket.emit("general_feedback", {"feedback":document.getElementById("generalFeedbackInput").value});
}

function sendErrorFeedback() {
    socket.emit("error_feedback", {"error":document.getElementById("errorFeedbackInput").value});
}