var socket = io.connect('http://localhost:5000');

var template = [];

function sendUpdate() {
    socket.emit("update_from_host", {"cookie" : getCookie("meeting_token")});
}

function getCookie(name) {
    const value =  `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function displayTemplate() {
    var HTMLString = "";

    for (i = 0; i < template.length; i++) {
        HTMLString += `<p>` + template[i].question + `</p>`;
    }

    document.getElementById("currentTemplate").innerHTML = HTMLString;
}

function updateTemplateDisplay() {
    socket.emit("template_update", "");
}

socket.on("template_update", function(data) {
    // data (json): {"questions":[{"question", "type"}]}
    var questions = data["questions"];
    var newQuestion;

    for (i = 0; i < questions.length; i++) {
        newQuestion = new Question(questions[i]["type"].type);
        newQuestion.setQuestion(questions[i]["question"]);
        template.push(newQuestion);
    }
    displayTemplate();
});

socket.on("connection_response", function(data) {
    if (data == "connected") {
        socket.emit("connect_as_host", {"cookie" : getCookie("meeting_token")});
    }
});

socket.on("meeting_details", function(data) {
    document.getElementById("meeting_code").innerHTML = data["meeting_code"];
    console.log("Message recieved");
});

socket.on("test_emit", function(data) {
    console.log(data);
});