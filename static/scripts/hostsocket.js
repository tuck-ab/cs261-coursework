var socket = io.connect('http://localhost:5000');

socket.on("connection_response", function(data) {
    if (data == "connected") {
        socket.emit("connect_as_host", {"cookie" : getCookie("meeting_token")})
    }
});

socket.on("meeting_details", function(data) {
    document.getElementById("meeting_code").innerHTML = data["meeting_code"];
    console.log("Message recieved");
});

socket.on("test_emit", function(data) {
    console.log(data);
});

function sendUpdate() {
    socket.emit("update_from_host", {"cookie" : getCookie("meeting_token")});
}

function getCookie(name) {
    const value =  `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}