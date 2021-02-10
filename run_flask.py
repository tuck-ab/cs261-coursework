import webserver
import websocket


if __name__ == "__main__":
    web_server_instance = webserver.WebServer("test")
    web_server_instance.run()