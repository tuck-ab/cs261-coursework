DROP TABLE IF EXISTS hosts;
CREATE TABLE hosts (
    hostid    INTEGER NOT NULL,
    socketid  TEXT NOT NULL,
    hostname  TEXT NOT NULL,
    hostpass  TEXT NOT NULL,
    salt      TEXT NOT NULL,
    PRIMARY KEY (hostid)
);

DROP TABLE IF EXISTS attendees;
CREATE TABLE attendees (
    attendeeid INTEGER NOT NULL,
    meetingid  INTEGER NOT NULL,
    socketid   TEXT NOT NULL,
    PRIMARY KEY (attendeeid, meetingid),
    FOREIGN KEY (meetingid) REFERENCES meetings(meetingid)
);

DROP TABLE IF EXISTS meetings;
CREATE TABLE meetings (
    meetingid  INTEGER NOT NULL,
    hostid     INTEGER NOT NULL,
    title      TEXT NOT NULL,
    runtime    INTEGER NOT NULL,
    PRIMARY KEY (meetingid),
    FOREIGN KEY (hostid) REFERENCES hosts(hostid)
);

DROP TABLE IF EXISTS feedback;
CREATE TABLE feedback (
    feedbackid    INTEGER NOT NULL,
    meetingid     INTEGER NOT NULL,
    attendeeid    INTEGER NOT NULL,
    feedbacktype  TEXT NOT NULL CHECK (feedbacktype IN ('error','question','response','mood')),
    anon          INTEGER NOT NULL CHECK (anon IN (0,1)),
    PRIMARY KEY (feedbackid),
    FOREIGN KEY (meetingid) REFERENCES meetings(meetingid),
    FOREIGN KEY (attendeeid) REFERENCES attendees(attendeeid)
);

DROP TABLE IF EXISTS errors;
CREATE TABLE errors (
    feedbackid  INTEGER NOT NULL,
    errortype   TEXT NOT NULL,
    errmessage  TEXT NOT NULL,
    PRIMARY KEY (feedbackid),
    FOREIGN KEY (feedbackid) REFERENCES feedback(feedbackid)
);

DROP TABLE IF EXISTS questions;
CREATE TABLE questions (
    feedbackid  INTEGER NOT NULL,
    qmessage    TEXT NOT NULL,
    PRIMARY KEY (feedbackid),
    FOREIGN KEY (feedbackid) REFERENCES feedback(feedbackid)
);

DROP TABLE IF EXISTS moods;
CREATE TABLE moods (
    moodid      INTEGER NOT NULL,
    feedbackid  INTEGER NOT NULL,
    moodtype    TEXT NOT NULL CHECK (moodtype IN ('text','emoji')),
    score       FLOAT NOT NULL,
    timeofmood  INTEGER NOT NULL,
    PRIMARY KEY (moodid),
    FOREIGN KEY (feedbackid) REFERENCES feedback(feedbackid)
);

DROP TABLE IF EXISTS text_moods;
CREATE TABLE text_moods (
    moodid      INTEGER NOT NULL,
    txtmessage  TEXT NOT NULL,
    PRIMARY KEY (moodid),
    FOREIGN KEY (moodid) REFERENCES moods(moodid)
);

DROP TABLE IF EXISTS emoji_moods;
CREATE TABLE emoji_moods (
    moodid     INTEGER NOT NULL,
    emojitype  TEXT NOT NULL,
    PRIMARY KEY (moodid),
    FOREIGN KEY (moodid) REFERENCES moods(moodid)
);

DROP TABLE IF EXISTS responses;
CREATE TABLE responses (
    responseid     INTEGER NOT NULL,
    feedbackid     INTEGER NOT NULL,
    responsetype   TEXT NOT NULL CHECK (responsetype IN ('text','emoji','multchoice')),
    questionasked  TEXT NOT NULL,
    PRIMARY KEY (responseid),
    FOREIGN KEY (feedbackid) REFERENCES feedback(feedbackid)
);

DROP TABLE IF EXISTS text_responses;
CREATE TABLE text_responses (
    responseid  INTEGER NOT NULL,
    txtmessage  TEXT NOT NULL,
    PRIMARY KEY (responseid),
    FOREIGN KEY (responseid) REFERENCES responses(responseid)
);

DROP TABLE IF EXISTS emoji_responses;
CREATE TABLE emoji_responses (
    responseid  INTEGER NOT NULL,
    emojitype   TEXT NOT NULL,
    PRIMARY KEY (responseid),
    FOREIGN KEY (responseid) REFERENCES responses(responseid)
);

DROP TABLE IF EXISTS mult_choice_responses;
CREATE TABLE mult_choice_responses (
    responseid      INTEGER NOT NULL,
    attendeeanswer  TEXT NOT NULL,
    PRIMARY KEY (responseid),
    FOREIGN KEY (responseid) REFERENCES responses(responseid)
);