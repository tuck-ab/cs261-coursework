var template = []

class Question {
    constructor(type) {
        this.type = type;
        this.question = "";
    }

    setQuestion(question) {
        this.question = question;
    }

    getJSONString() {
        return "{\"question\":\"" + this.question + "\"}"
    }
}

function openPopup() {
    document.getElementById("createQuestion").style.display = "block";
}

function closePopup() {
    document.getElementById("createQuestion").style.display = "none";
}

function questionTypeUpdate() {
    var questionType = document.getElementById("questionType").value;
    var inputer = document.getElementById("questionInputer");

    if (questionType === "normal") {
        var htmlString = `<input type"text" id="mainQuestion" name="mainQuestion"><br>`;
        htmlString += `<input type="button" onclick="submitNormalQuestion()" value="Submit">`;
        
        inputer.innerHTML = htmlString;
    }
}

function submitNormalQuestion() {
    addNormalQuestion(document.getElementById("mainQuestion").value);
    closePopup();
}

function addNormalQuestion(question) {
    var newQuestion = new Question("normal");
    newQuestion.setQuestion(question);
    template.push(newQuestion);
    updateTemplateDisplay();
}

function updateTemplateDisplay() {
    var htmlTemplate = document.getElementById("template-display");

    var htmlString = "";
    var loopString = "";

    for (i = 0; i < template.length; i++) {
        loopString = "<p>" + template[i].question + "</p>"

        htmlString = htmlString + loopString;
    }

    htmlTemplate.innerHTML = htmlString;
}

function getTemplateJSONString() {
    var JSONString = "{\"questions\":[";

    for (i = 0; i < template.length; i++) {
        JSONString += template[i].getJSONString() + ",";
    }

    JSONString = JSONString.substring(0, JSONString.length - 1) + "]}";
    console.log(JSONString);
    return JSONString
}

function submitTemplate() {
    var url = window.location.href;

    var form = document.createElement("form");
    form.method = "post";
    form.action = url;

    var hiddenInput = document.createElement("input");
    hiddenInput.type = "hidden";
    hiddenInput.name = "templateJSON";
    hiddenInput.value = getTemplateJSONString();
    form.appendChild(hiddenInput);

    document.body.appendChild(form);
    form.submit();

}