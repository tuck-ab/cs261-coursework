var template = []

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