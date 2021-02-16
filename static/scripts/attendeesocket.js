var socket = io.connect('http://localhost:5000');

socket.on("connection_response", function(data) {
    if (data == "connected") {
        socket.emit("connect_as_attendee", {"code" : meetingcode})
    }
});

socket.on("meeting_details", function(data) {
    if (data["connection_status"] == "connected") {
        document.getElementById("connection_status").innerHTML = "Connected to room " + meetingcode.toString();
    } else {
        document.getElementById("connection_status").innerHTML = "Connection failed";
    }
    console.log("message_recieved");
});

socket.on("update_from_server", function (data) {
    console.log(data);
});

function sendTest() {
    console.log("test sending");
    socket.emit("question_response", {"data":document.getElementById("test").value});
}