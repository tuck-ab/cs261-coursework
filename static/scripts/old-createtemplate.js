var finalTemplate = [];

class Question {
    constructor(type) {
        this.type = type;
        this.question = "";
        this.answers = [];
    }

    setQuestion(question) {
        this.question = question;
    }

    addAnswer(answer) {
        this.answers.push(answer);
    }
}

function closePopup() {
    document.getElementById("createQuestion").style.display = "none";
}

function addQuestion() {
    document.getElementById("createQuestion").style.display = "block";
}

function clearQuestionForm() {
    var form = document.getElementById("questionform");
    [].forEach.call(form.childNodes, function (child) {
        form.removeChild(child);
    });
}

function choiceUpdate() {
    var new_choice = document.getElementById("questionType").value;
    clearQuestionForm();
    var form = document.getElementById("questionform");
    if (new_choice === "question") {
        var questionLabel = document.createElement("label");
        questionLabel.innerHTML = "Question: ";

        var questionInput = document.createElement("input");
        questionInput.type = "text";
        questionInput.id = "question";

        var confirmButton = document.createElement("input");
        confirmButton.type = "button";
        confirmButton.id = "confirmbutton";
        confirmButton.value = "confirm"
        confirmButton.onclick = confirmQuestion;

        form.appendChild(questionLabel);
        form.appendChild(document.createElement("br"));
        form.appendChild(questionInput);
        form.appendChild(document.createElement("br"));
        form.appendChild(confirmButton);
    }

}

function confirmQuestion() {
    closePopup();
    var questionType = document.getElementById("questionType").value;
    var questionForm = document.getElementById("questionform");

    var questionObject = new Question(questionType);
    questionObject.setQuestion(questionForm.getElementsById("question"));

    console.log("Question confirmed");
}

function updateTemplateBox() {
    var templateBox = document.getElementById()
}