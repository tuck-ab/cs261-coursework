var ws = new WebSocket("ws://127.0.0.1:5678/"),
    messages = document.createElement('ul');
function sendMsg() {
    var data = {};
    data["name"] = document.getElementById("name").value;
    data["msg"] = document.getElementById("msg").value;
    ws.send(JSON.stringify(data));
};
ws.onmessage = function(event) {
    document.getElementById("response").innerHTML = event.data;
};