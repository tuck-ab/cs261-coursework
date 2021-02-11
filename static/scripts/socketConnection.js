var socket = io.connect('http://localhost:5000');
        
socket.on('connection_response', function(msg) {
    console.log('After connect', msg);
});

function joinMeeting() {
    var code = document.getElementById("meetingCode").value;
    socket.emit("join_meeting", code);
}