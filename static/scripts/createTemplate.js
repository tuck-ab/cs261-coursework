var questionTemplate = new QuestionTemplate();

function submitTemplate() {
    var url = window.location.href;

    var titleElement = document.getElementById("meetingTitle");
    if (titleElement.value == "") {
        alert("Please set host name");
        return false
    }

    var form = document.createElement("form");
    form.method = "post";
    form.action = url;

    var templateHiddenInput = document.createElement("input");
    templateHiddenInput.type = "hidden";
    templateHiddenInput.name = "templateJSON";
    templateHiddenInput.value = questionTemplate.getJSONString();
    form.appendChild(templateHiddenInput);

    var hostHidenInput = document.createElement("input");
    hostHidenInput.type = "hidden";
    hostHidenInput.name = "title";
    hostHidenInput.value = titleElement.value;
    form.appendChild(hostHidenInput);

    document.body.appendChild(form);
    form.submit();

}

function translateQuestions(questions) {
    questionTemplate = new QuestionTemplate();
    var newQuestion;
    var optionList;

    for (var i = 0; i < questions.length; i++) {
        if (questions[i]["type"] == "normal") {
            newQuestion = new Question("normal");
            newQuestion.setQuestion(questions[i]["question"]);
            
        } else {
            newQuestion = new Question("multichoice");
            newQuestion.setQuestion(questions[i]["question"]);
            optionList = questions[i]["options"];
            for (var j = 0; j < optionList.length; j++) {
                newQuestion.addChoice(optionList[j]);
            }
        }

        questionTemplate.addQuestion(newQuestion);
    }

    return questionTemplate
}

function setTemplate1() {
    var template = [{"type":"normal", "question": "What did you like about the event?"},
                    {"type":"normal", "question": "How do you think the event could be improved?"},
                    {"type":"normal", "question": "What is your biggest takeaway?"},
                    {"type":"normal", "question": "Is there anything else you want to share about the event?"},
                    {"type":"multichoice", "question":"How would you rate the content of the event?", "options": ["Excellent", "Very Good","Good","Fair","Poor"]},
                    {"type":"multichoice", "question":"How organised is the event?", "options": ["Extremely Organised", "Very Organised","Somewhat Organised","Not Very Organised","Not Organised At All"]},
                    {"type":"multichoice", "question":"How interactive is the host of the event?", "options": ["Extremely Interactive", "Very Interactive","Somewhat Interactive","Not Very Interactive","Not Interactive At All"]},
                    {"type":"multichoice", "question":"Did the event meet your expectations?", "options": ["Yes", "No"]},
                    {"type":"multichoice", "question":"How was the pace of the event?", "options": ["Too fast", "Good", "Slow"]},
                    {"type":"multichoice", "question":"Could you hear and understand the speaker?", "options": ["Yes", "No"]}];

    questionTemplate = translateQuestions(template);
    onTemplateUpdate();

}

function setTemplate2() {
    var template = [{"type":"normal", "question": "What did you find helpful about the session?"},
                    {"type":"normal", "question": "What do you think needs to be improved?"},
                    {"type":"normal", "question": "Do you have any other comments?"},
                    {"type":"multichoice", "question":"How was the content of the session?", "options": ["Too Much", "Good Amount", "Not enough"]},
                    {"type":"multichoice", "question":"How much of the content was new?", "options": ["All", "Most", "Half", "Some", "None"]},
                    {"type":"multichoice", "question":"How much were you able to understand?", "options": ["All", "Most", "Half", "Some", "None"]},
                    {"type":"multichoice", "question":"How was the pace of the session?", "options": ["Too Fast", "Good", "Too Slow"]}];
    
    questionTemplate = translateQuestions(template);
    onTemplateUpdate();
}

function setTemplate3() {
    var template = [{"type":"normal", "question": "What did you find helpful about the session?"},
                    {"type":"normal", "question": "What do you think needs to be improved?"},
                    {"type":"normal", "question": "Do you have any other comments?"},
                    {"type":"normal", "question": "How did the session benifit/not-benefit you?"},
                    {"type":"multichoice", "question":"How was the content of the session?", "options": ["Too Much", "Good Amount", "Not enough"]},
                    {"type":"multichoice", "question":"How much of the content was new?", "options": ["All", "Most", "Half", "Some", "None"]},
                    {"type":"multichoice", "question":"How much were you able to understand?", "options": ["All", "Most", "Half", "Some", "None"]},
                    {"type":"multichoice", "question":"How was the pace of the session?", "options": ["Too Fast", "Good", "Too Slow"]},
                    {"type":"multichoice", "question":"Was there enough support available?", "options": ["Yes", "No"]}]
    
    questionTemplate = translateQuestions(template);
    onTemplateUpdate();
}

function onTemplateUpdate() {
    questionTemplate.displayTemplate(document.getElementById("templateDisplay"));
}