var multChoiceCreate = new MultChoiceCreate();

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
<<<<<<< HEAD
        var htmlString = `<input type="text" id="mainQuestion" name="mainQuestion"><br>`;
        htmlString += `<input type="button" onclick="submitNormalQuestion()" value="Submit">`;   
    }
    if (questionType === "multichoice") {
        var htmlString = `<input type="text" id="mainQuestion" name="mainQuestion"><br>`;
        htmlString += `<input type="text" id="option1" name="option1"><br>`;
        htmlString += `<input type="text" id="option2" name="option2"><br>`;
        htmlString += `<input type="button" onclick="addAdditionalChoice()" value="Add More Choices">`;
        htmlString += `<input type="button" onclick="submitMultiChoiceQuestion()" value="Submit">`;
    }

    inputer.innerHTML = htmlString;
=======
        var htmlString = `<input type"text" id="mainQuestion" name="mainQuestion"><br>`;
        htmlString += `<input type="button" onclick="submitNormalQuestion()" value="Submit">`;
        inputer.innerHTML = htmlString;
    }
    else {
        multChoiceCreate = new MultChoiceCreate();
        var htmlString = `<p>Question: <input type="text" id="mainQuestion" name="mainQuestion"></p>`;
        htmlString += `<div id="multOptions"></div>`;

        htmlString += `<input type="button" onclick="addOption()" value="Add another option">`;
        htmlString += `<input type="button" onclick="submitMultiChoiceQuestion()" value="Submit">`;
        inputer.innerHTML = htmlString;

        multChoiceCreate.display(document.getElementById("multOptions"));
    }
        
}

function addOption() {
    multChoiceCreate.addOption();
    multChoiceCreate.display(document.getElementById("multOptions"));
}

function updateOption(id) {
    multChoiceCreate.updateOption(id, document.getElementById("option" + id.toString()).value);
}

function removeOption(id) {
    multChoiceCreate.removeOption(id);
    multChoiceCreate.display(document.getElementById("multOptions"));
<<<<<<< HEAD
>>>>>>> b1d8a05f0a6aac0077351ecd05c6583236fb346a
=======
>>>>>>> b1d8a05f0a6aac0077351ecd05c6583236fb346a
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
<<<<<<< HEAD
<<<<<<< HEAD
    for (var i = 1; i < counter + 1; i++) {
        newQuestion.addChoice(document.getElementById("option"+i).value);
        }
=======
=======
>>>>>>> b1d8a05f0a6aac0077351ecd05c6583236fb346a

    for (var i = 0; i < multChoiceCreate.options.length; i++) {
        newQuestion.addChoice(multChoiceCreate.options[i]);
    }

<<<<<<< HEAD
>>>>>>> b1d8a05f0a6aac0077351ecd05c6583236fb346a
=======
>>>>>>> b1d8a05f0a6aac0077351ecd05c6583236fb346a
    questionTemplate.addQuestion(newQuestion);
    onTemplateUpdate();
    closePopup();
}

function addAdditionalChoice() {
    counter += 1;
    var inputer = document.getElementById("questionInputer");
    inputer.innerHTML += `<input type="text" id="option`+ counter.toString() +`"  name="option`+ counter.toString() +`"><br>`;
}

