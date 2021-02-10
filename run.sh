#!/bin/bash

echo "Launching the Flask Server"
echo

python3 run_flask.py &

echo
echo "Launching Socket Server"
echo

python3 run_sockets.py &

ServerID=$(ps -aux | grep "run_flask.py" | awk '{ if ($11 == "python3") {print $2} }')
SocketID=$(ps -aux | grep "run_sockets.py" | awk '{ if ($11 == "python3") {print $2} }')

trap 'echo "Exiting";kill "$ServerID";kill "$SocketID"; exit 0' INT
while [ true ]; do 
    :
done
