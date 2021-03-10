import os
import json
import time

from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_socketio import SocketIO, emit, join_room, leave_room

from classes import *

controller = Meeting_Controller()
db_conn = DBController()

app = Flask(__name__)
app.config["SECRET_KEY"] = "SecretKey"

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

## -- Mapping pages

@app.route("/")
def index():
    """
    Renders and returns the index page to a client when they connect to the website
    """
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        new_token = db_conn.check_host(username, password)

        if new_token is None:
            return "<h1>Wrong credentials</h1>"
        else:
            resp = make_response(redirect(url_for("index")))
            resp.set_cookie("accessToken", new_token)

            return resp

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        token = db_conn.add_new_host(username, password)

        if token is None:
            token="token failed"

        resp = make_response(redirect(url_for("index")))
        resp.set_cookie("accessToken", token)

        return resp

@app.route("/search")
def search_page():
    if request.method == "GET":
        token = request.cookies.get("accessToken")
        
        if token == None or not db_conn.check_token(token):
            return redirect(url_for("login"))

        return render_template("search.html")

@app.route("/meeting_search", methods=["POST"])
def search_query():

    token = request.cookies.get("accessToken")
    meetings_list = db_conn.get_meetings(token)
    results_list = []
    for meetings in meetings_list:
        search_result = {
            "title": meetings[0],
            "date_time": meetings[1],
            "meeting_id": meetings[2],
            "run_time": meetings[3],
        }
        
        results_list.append(search_result)

    return {"results": results_list}

@app.route("/meeting_submit", methods=["POST"])
def choose_meeting():
    meeting = json.loads(request.form["meeting"])
    meeting_id = meeting["meetingid"]
    token = request.cookies.get("accessToken")

    information = db_conn.get_meeting_info(meeting_id, token)
    if information is None:
        return "Invalid access token"
    else:
        return information

        text_over_time = text_sentiment_over_time(meeting_id)
        emoji_over_time = emoji_sentiment_over_time(meeting_id)

@app.route("/create", methods=["GET","POST"])
def create_meeting():
    """
    Deals with requests for the URL/create page

    If the request is a GET request then it returns the webpage to the client

    If the request is a POST request then it deals with the template recieved and redirects
    the client to the 'host' page for a meeting along with the necessary identifiers as cookies.
    """
    token = request.cookies.get("accessToken")
    if request.method == "GET":
        
        if token == None or not db_conn.check_token(token):
            return redirect(url_for("login"))

        return render_template("create.html")

    elif request.method == "POST":
        template = Template().from_json(json.loads(request.form["templateJSON"]))

        title = request.form["title"]
        
        ## -- Make new meeting
        new_meeting = controller.create_meeting(db_conn)
        new_meeting.set_template(template)
        new_meeting.title = title

        db_conn.insert_meeting(new_meeting.host_token, token, title)

        ## -- Send the response with token
        resp = make_response(redirect(url_for("host_page")))
        resp.set_cookie("meeting_token", new_meeting.host_token)
        return resp

@app.route("/join", methods=["POST"])
def join_meeting():
    """
    Deals with POST request to the URL/join page

    Redirects the client to the 'attendee_page' adding the room code to the HTML
    """
    code = request.form["meetingCode"]

    return redirect(url_for("attendee_page", code=code))

@app.route("/meeting/host")
def host_page():
    """
    Renders and returns the page for a meeting's host
    """
    return render_template("host.html") 

@app.route("/meeting/attendee/<code>")
def attendee_page(code):
    """
    Renders and returns the page for a meeting's attendee
    """
    return render_template("attendee.html", meeting_code=code)

@app.route("/meetingend")
def meeting_end():
    return render_template("meetingEnded.html")

## -- Web Socket functions

@socketio.on("connect")
def connected():
    """
    Function called when a user first connects to the socket.

    Sends back a response to verify the connection and to trigger any required
    client side functions.
    """
    emit("connection_response", "connected")

@socketio.on("connect_as_host")
def host_connect(data):
    """
    Used when the host responds to the connected message

    Works out which room the host is using and sends back necessary details eg. room code
    """
    cookie = data["cookie"]
    meeting = controller.get_meeting_from_token(cookie)

    new_host = Host(request.sid, meeting=meeting)
    meeting.set_host(new_host)
    join_room(new_host.get_room())
    join_room(meeting.host_room)

    emit("meeting_details", {"meeting_code":meeting.code})
    emit("template_update", meeting.get_template().get_json())

@socketio.on("connect_as_attendee")
def attendee_connect(data):
    """
    Used when the attendee responds to the connected message

    Works out which room the attendee is using and sends back necessary details eg. question template
    """
    to_send_back = {}

    code = data["code"]
    meeting = controller.get_meeting_from_code(str(code))
    
    if meeting:
        to_send_back["connection_status"] = "connected"

        new_attendee = Attendee(request.sid, meeting=meeting)
        meeting.add_attendee(new_attendee)
        join_room(new_attendee.get_room())
        join_room(meeting.attendee_room)
        
        to_send_back["template"] = meeting.get_template().get_json()
        to_send_back["title"] = meeting.title

    else:
        to_send_back["connection_status"] = "not_connected"

    emit("meeting_details", to_send_back)

@socketio.on("update_from_host")
def update_from_host(data):
    meeting = controller.get_meeting_from_token(data["cookie"])

    emit("update_from_server", {"test":"testmsg"}, room=meeting.attendee_room)

@socketio.on("template_update")
def template_update(data):
    meeting = controller.get_meeting_from_token(data["cookie"])
    questions = json.loads(data["template"])

    meeting.get_template().from_json(questions)

    emit("template_update", meeting.get_template().get_json())
    emit("template_update", {"template": meeting.get_template().get_json()}, room=meeting.attendee_room)

@socketio.on("mult_choice_response")
def mult_choice_response(data):
    """
    Function called when the attendee sends an multiple choice response during the presentation

    Parameters:
        data (dict) :JSON data from the socket connection 
                    {'question': '{"question":question(str), "type": type(str), "options": options(list of str)}', 'answer': answer(str)}
    """
    attendee = controller.get_attendee(request.sid)
    meeting = controller.get_meeting_from_attendee(request.sid)
    question = json.loads(data["question"])
    options = question["options"]
    answer = data["answer"]

    mult_choice_feedback = MultChoiceResponse(attendee.get_sid(), meeting.get_token(), "multchoice", question["question"], answer)
    
    db_conn.insert_response(mult_choice_feedback)

    results_frequency = db_conn.mult_choice_frequency(question["question"])
    result_list = []
    for i in results_frequency:
        result_list.append(i[0])

    zero_freq = list(set(options) - set(result_list))

    for j in zero_freq:
        results_frequency.append((j,0))

    emit("mult_choice_response", {"question":question["question"], "results": results_frequency}, room=meeting.host_room)
    

@socketio.on("question_response")
def question_response(data):
    """
    Function called when an attendee responds to a normal question.
    TODO - Sends the data to be analysed and emits any change to the host

    Parameters:
        data (dict): JSON data from the socket connection
                     {"question": question(dict), "answer": answer(str)}

    """
    attendee = controller.get_attendee(request.sid)
    meeting = controller.get_meeting_from_attendee(request.sid)
    question = json.loads(data["question"])
    answer = data["answer"]

    text_response = TextResponse(attendee.get_sid(), meeting.get_token(), "text", question["question"], answer)

    db_conn.insert_response(text_response)

    emit("question_answer_response", {"question": question["question"], "answer": answer}, room=meeting.host_room)

@socketio.on("emoji_response")
def emoji_response(data):
    """
    Function called when the attendee sends an emoji response during the presentation

    Parameters:
        data (dict) :JSON data from the socket connection 
                    {"emoji":emoji score(number)}
    """
    emoji = data["emoji"]
    attendee = controller.get_attendee(request.sid)
    meeting = controller.get_meeting_from_attendee(request.sid)
    emoji_analyser = meeting.get_emoji_sentiment_analyser()
    emoji_analyser.set_emoji_sentiment(emoji)
    emoji_score = emoji_analyser.get_emoji_sentiment()
    host = meeting.get_host()

    emoji_analyser.set_average_emoji_sentiment()

    emoji_mood = EmojiMood(attendee.get_sid(), meeting.get_token(), "emoji", emoji_score, time.time(), emoji_analyser.get_percentage(), emoji)

    db_conn.insert_mood(emoji_mood)

    emit("emoji_response", {"emoji":emoji_mood.get_mood_emoji(), "emoji_score":emoji_analyser.get_percentage()}, room=meeting.host_room)

@socketio.on("general_feedback")
def general_feedback(data):
    """
    Function called when the attendee sends general feedback during the presentation
    TODO - Sends the data to be analysed and emits any change to the host

    Parameters:
        data (dict): JSON data from the socket connection
                     {"feedback": feedback(str)}
    """
    feedback = data["feedback"]
    attendee = controller.get_attendee(request.sid)
    meeting = controller.get_meeting_from_attendee(request.sid)
    analyser = meeting.get_sentiment_analyser()
    analyser.set_sentiment(feedback)
    score = analyser.get_sentiment()
    host = meeting.get_host()

    analyser.set_average_sentiment()

    text_mood = TextMood(attendee.get_sid(), meeting.get_token(), "text", score, time.time(), analyser.get_percentage(), feedback)
    
    db_conn.insert_mood(text_mood)

    emit("feedback_response", {"feedback":text_mood.get_mood_text(), "score":analyser.get_percentage()}, room=meeting.host_room)

@socketio.on("error_feedback")
def error_feedback(data):
    """
    Function called when the attendee reports an error to the host during a presentation
    TODO - Sends the error to the database

    Parameters:
        data (dict): JSON data from the socket connection
                     {"error": error{str}}
    """
    error = data["error"]
    attendee = controller.get_attendee(request.sid)
    meeting = controller.get_meeting_from_attendee(request.sid)
    host = meeting.get_host()

    error_feedback = ErrorFeedback(attendee.get_sid(), meeting.get_token(), "general error", error)

    db_conn.insert_error(error_feedback)

    emit("error_response", {"error":error_feedback.get_error_message()}, room=meeting.host_room)

def text_sentiment_over_time(meetingid):
    text_sentiment_results = db_conn.sentiment_history("text",meetingid)
    return text_sentiment_results

def emoji_sentiment_over_time(meetingid):
    emoji_sentiment_results = db_conn.sentiment_history("emoji",meetingid)
    return emoji_sentiment_results

@socketio.on("disconnect")
def disconnected():
    host = controller.get_host_from_sid(request.sid)
    if host != None:
        db_conn.update_runtime(host.get_meeting().host_token)
    else:
        attendee = controller.get_attendee(request.sid)
        if attendee != None:
            meeting = controller.get_meeting_from_attendee(request.sid)
            meeting.attendees.pop(attendee.sid)

@socketio.on("end_meeting")
def end_meeting(data):
    meeting = controller.get_meeting_from_host(controller.get_host_from_sid(request.sid))
    emit("meeting_ended","string", room=meeting.attendee_room)
    emit("meeting_ended", "string", room=meeting.host_room)
    
## -- Running the server
if __name__ == "__main__":
    socketio.run(app)