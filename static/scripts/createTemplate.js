var questionTemplate = new QuestionTemplate();

function submitTemplate() {
    var url = window.location.href;

    var nameElement = document.getElementById("hostName");
    if (nameElement.value == "") {
        alert("Please set host name");
        return false
    }

    var keyWordElement = document.getElementById("hostKeyWord");
    if (keyWordElement.value == "") {
        alert("Please set key word");
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
    hostHidenInput.name = "hostInfo";
    hostHidenInput.value = `{"name":"` + nameElement.value + `","keyword":"` + keyWordElement.value + `"}`;
    form.appendChild(hostHidenInput);

    document.body.appendChild(form);
    console.log("submitting");
    alert("pause");
    form.submit();

}

function onTemplateUpdate() {
    questionTemplate.displayTemplate(document.getElementById("templateDisplay"));
}