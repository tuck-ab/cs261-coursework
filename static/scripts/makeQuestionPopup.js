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
    }
    else {
        var htmlString = `<input type="text" id="mainQuestion" name="mainQuestion"><br>`;
        htmlString += `<input type="text" id="choice 1" name="choice 1"><br>`;
        htmlString += `<input type="text" id="choice 2" name="choice 2"><br>`;
        htmlString += `<input type="text" id="choice 3" name="choice 3"><br>`;
        htmlString += `<input type="text" id="choice 4" name="choice 4"><br>`;
        htmlString += `<input type="button" onclick="submitMultiChoiceQuestion()" value="Submit">`;  
    }
        
        inputer.innerHTML = htmlString;
}


function submitNormalQuestion() {
    addNormalQuestion(document.getElementById("mainQuestion").value);
    onTemplateUpdate();
    closePopup();
}

function addNormalQuestion(question) {
    var newQuestion = new Question("normal");
    newQuestion.setQuestion(question);
    questionTemplate.addQuestion(newQuestion);
}

function submitMultiChoiceQuestion() {
    var newQuestion = new Question("multichoice");
    newQuestion.setQuestion(document.getElementById("mainQuestion").value);
    for (var i = 1; i < 5; i++) {
        newQuestion.addChoice(document.getElementById("choice "+i).value);
        }
    questionTemplate.addQuestion(newQuestion);
    onTemplateUpdate();
    closePopup();
}

