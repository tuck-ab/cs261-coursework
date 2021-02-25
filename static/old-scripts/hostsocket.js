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
    console.log(template);
}

function getTemplateJSONString() {
    var JSONString = "{\"questions\":[";

    for (i = 0; i < template.length; i++) {
        JSONString += template[i].getJSONString() + ",";
    }

    JSONString = JSONString.substring(0, JSONString.length - 1) + "]}";
    return JSONString
}

function updateTemplateDisplay() {
    socket.emit("template_update", {"cookie":getCookie("meeting_token"), "template": getTemplateJSONString()});
}

socket.on("template_update", function(data) {
    // data (json): {"questions":[{"question", "type"}]}
    var questions = data["questions"];
    var newQuestion;

    template = [];

    for (i = 0; i < questions.length; i++) {
        newQuestion = new Question(questions[i]["type"]);
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

class CurrentErrors {
    constructor() {
        this.errors = [];
    }

    addError(error) {
        this.errors.push(error);
    }

    getDisplayString() {
        var outString = "";

        for (i = 0; i < this.errors.length; i++) {
            outString += `<p>` + this.errors[i] + `</p>`
        }

        return outString;
    }
}

var currentErrors = new CurrentErrors()

socket.on("error_response", function(data) {
    var errorDisplay = document.getElementById("errorFeedbackDisplay");
    currentErrors.addError(data["error"]);
    errorDisplay.innerHTML = currentErrors.getDisplayString();
});

socket.on("test_emit", function(data) {
    console.log(data);
});