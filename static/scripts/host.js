var questionTemplate = new QuestionTemplate();
var errorDisplay = new ErrorDisplay();
var feedbackDisplay = new FeedbackDisplay();
var questionAnswerDisplay = new QuestionAnswerDisplay();

function getCookie(name) {
    const value =  `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function endMeeting() {
    socket.emit("end_meeting", "meaningless string");
}

function onTemplateUpdate() {
    socket.emit("template_update", {"cookie":getCookie("meeting_token"), "template": questionTemplate.getJSONString()});
}

socket.on("template_update", function(data) {
    questionTemplate.fromJSON(data);
    questionTemplate.displayTemplate(document.getElementById("currentTemplate"))
});

socket.on("connection_response", function(data) {
    if (data == "connected") {
        socket.emit("connect_as_host", {"cookie" : getCookie("meeting_token")});
    }
});

socket.on("meeting_ended", function(data) {
    var sections = window.location.href.split("/")
    var counter = 0;
    var newURL = "";

    while (counter < sections.length && sections[counter] !== "meeting") {
        newURL += sections[counter] + "/";
        counter += 1
    }

    window.location.href = newURL + "meetingend";
})

socket.on("meeting_details", function(data) {
    document.getElementById("meeting_code").innerHTML = data["meeting_code"];
});

socket.on("question_answer_response", function(data) {
    questionAnswerDisplay.addQuestionAnswerPair(data["question"], data["answer"]);
    questionAnswerDisplay.displayQuestionAnswer(document.getElementById("questionAnswerDisplay"));
    console.log(questionAnswerDisplay.questionAnswerList);
});

socket.on("feedback_response", function(data) {
    feedbackDisplay.addFeedback(data["feedback"]);
    feedbackDisplay.displayFeedback(document.getElementById("recentFeedbackDisplay"));
    document.getElementById("sentimentScore").innerHTML = data["score"];
});

socket.on("error_response", function(data) {
    errorDisplay.addError(data["error"]);
    errorDisplay.displayErrors(document.getElementById("errorFeedbackDisplay"));
});

function removeError(id) {
    errorDisplay.removeError(id);
    errorDisplay.displayErrors(document.getElementById("errorFeedbackDisplay"));
}