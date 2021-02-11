var socket = io.connect('http://localhost:5000');
        
socket.on('connection_response', function(msg) {
    console.log('After connect', msg);
});