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

function onTemplateUpdate() {
    questionTemplate.displayTemplate(document.getElementById("templateDisplay"));
}