var questionTemplate = new QuestionTemplate();

function submitTemplate() {
    var url = window.location.href;

    var form = document.createElement("form");
    form.method = "post";
    form.action = url;

    var hiddenInput = document.createElement("input");
    hiddenInput.type = "hidden";
    hiddenInput.name = "templateJSON";
    hiddenInput.value = questionTemplate.getJSONString();
    form.appendChild(hiddenInput);

    document.body.appendChild(form);
    form.submit();

}

function onTemplateUpdate() {
    questionTemplate.displayTemplate(document.getElementById("templateDisplay"));
}