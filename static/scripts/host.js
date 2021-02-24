var questionTemplate = new QuestionTemplate();

function getCookie(name) {
    const value =  `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function sendUpdate() {
    socket.emit("update_from_host", {"cookie" : getCookie("meeting_token")});
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

socket.on("meeting_details", function(data) {
    document.getElementById("meeting_code").innerHTML = data["meeting_code"];
});

socket.on("error_response", function(data) {
    var errorDisplay = document.getElementById("errorFeedbackDisplay");
    console.log(data);
});