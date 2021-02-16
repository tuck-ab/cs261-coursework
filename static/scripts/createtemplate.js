function closePopup() {
    document.getElementById("createQuestion").style.display = "none";
}

function addQuestion() {
    document.getElementById("createQuestion").style.display = "block";
}

function choiceUpdate() {
    var new_choice = document.getElementById("questionType").value;
    console.log(new_choice);
    
}