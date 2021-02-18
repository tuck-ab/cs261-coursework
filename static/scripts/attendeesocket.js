var socket = io.connect('http://localhost:5000');

class HostQuestions {
    constructor() {
        this.questions = [];
    }

    updateDisplay() {
        // Normal question: <p>Question</p><input type="text" id=""><input type="button" onclick="sendQuestion(id)" value="Send">

        var HTMLString = "";
        var loopString;

        for (var i = 0; i < this.questions.length; i++) {
            loopString = "<p>" + this.questions[i].question + "</p>";
            loopString += `<input type="text" id="question_` + i.toString() +`">`;
            loopString += `<input type="button" onclick="sendQuestionAnswer(` + i.toString() + `)" value="Send"><br>`;

            HTMLString += loopString;
        }

        document.getElementById("hostQuestions").innerHTML = HTMLString;
    }

    setQuestionsFromJSON(JSONObj) {
        var newQuestion;

        for (var i = 0; i < JSONObj["questions"].length; i++) {
            newQuestion = new Question(JSONObj["questions"][i]["type"]);
            newQuestion.setQuestion(JSONObj["questions"][i]["question"]);
            this.questions.push(newQuestion);
        }
    }
}

var hostQuestions = new HostQuestions();

socket.on("connection_response", function(data) {
    if (data == "connected") {
        socket.emit("connect_as_attendee", {"code" : meetingcode});
    }
});

socket.on("meeting_details", function(data) {
    if (data["connection_status"] == "connected") {
        document.getElementById("connection_status").innerHTML = "Connected to room " + meetingcode.toString();
        console.log(data["template"]);
        hostQuestions.setQuestionsFromJSON(data["template"]);
        hostQuestions.updateDisplay();
    } else {
        document.getElementById("connection_status").innerHTML = "Connection failed";
    }
    console.log("message_recieved");
});

socket.on("update_from_server", function (data) {
    console.log(data);
});

function sendGeneralFeedback() {
    socket.emit("general_feedback", {"feedback":document.getElementById("generalFeedbackInput").value});
}

function sendQuestionAnswer(id) {
    var answer = document.getElementById("question_" + id).value;
    socket.emit("question_response", {"question":hostQuestions.questions[Number(id)].getJSONString(), "answer":answer})
}

function sendTest() {
    console.log("test sending");
    socket.emit("question_response", {"data":document.getElementById("test").value});
}