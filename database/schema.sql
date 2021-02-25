DROP TABLE IF EXISTS hosts;
CREATE TABLE hosts (
    hostid  INTEGER NOT NULL,
    PRIMARY KEY (hostid)
);

DROP TABLE IF EXISTS attendees;
CREATE TABLE attendees (
    attendeeid INTEGER NOT NULL,
    meetingid  INTEGER NOT NULL,
    PRIMARY KEY (attendeeid, meetingid),
    FOREIGN KEY (meetingid) REFERENCES meetings(meetingid)
);

DROP TABLE IF EXISTS meetings;
CREATE TABLE meetings (
    meetingid  INTEGER NOT NULL,
    hostid     INTEGER NOT NULL,
    title      VARCHAR(30) NOT NULL,
    runtime    INTEGER NOT NULL,
    PRIMARY KEY (meetingid),
    FOREIGN KEY (hostid) REFERENCES hosts(hostid)
);

DROP TABLE IF EXISTS feedback;
CREATE TABLE feedback (
    feedbackid    INTEGER NOT NULL,
    meetingid     INTEGER NOT NULL,
    attendeeid    INTEGER NOT NULL,
    feedbacktype  VARCHAR(8) NOT NULL CHECK (feedbacktype IN ('error','question','response','mood')),
    anon          INTEGER NOT NULL CHECK (anon IN (0,1)),
    PRIMARY KEY (feedbackid),
    FOREIGN KEY (meetingid) REFERENCES meetings(meetingid),
    FOREIGN KEY (attendeeid) REFERENCES attendees(attendeeid)
);

DROP TABLE IF EXISTS errors;
CREATE TABLE errors (
    feedbackid  INTEGER NOT NULL,
    errortype   VARCHAR(20) NOT NULL,
    errmessage  VARCHAR(50) NOT NULL,
    PRIMARY KEY (feedbackid),
    FOREIGN KEY (feedbackid) REFERENCES feedback(feedbackid)
);

DROP TABLE IF EXISTS questions;
CREATE TABLE questions (
    feedbackid  INTEGER NOT NULL,
    qmessage    VARCHAR(50) NOT NULL,
    PRIMARY KEY (feedbackid),
    FOREIGN KEY (feedbackid) REFERENCES feedback(feedbackid)
);

DROP TABLE IF EXISTS moods;
CREATE TABLE moods (
    moodid      INTEGER NOT NULL,
    feedbackid  INTEGER NOT NULL,
    moodtype    VARCHAR(5) NOT NULL CHECK (moodtype IN ('text','emoji')),
    score       FLOAT NOT NULL,
    timeofmood  INTEGER NOT NULL,
    PRIMARY KEY (moodid),
    FOREIGN KEY (feedbackid) REFERENCES feedback(feedbackid)
);

DROP TABLE IF EXISTS text_moods;
CREATE TABLE text_moods (
    moodid      INTEGER NOT NULL,
    txtmessage  VARCHAR(50) NOT NULL,
    PRIMARY KEY (moodid),
    FOREIGN KEY (moodid) REFERENCES moods(moodid)
);

DROP TABLE IF EXISTS emoji_moods;
CREATE TABLE emoji_moods (
    moodid     INTEGER NOT NULL,
    emojitype  VARCHAR(30) NOT NULL,
    PRIMARY KEY (moodid),
    FOREIGN KEY (moodid) REFERENCES moods(moodid)
);

DROP TABLE IF EXISTS responses;
CREATE TABLE responses (
    responseid     INTEGER NOT NULL,
    feedbackid     INTEGER NOT NULL,
    responsetype   VARCHAR(10) NOT NULL CHECK (responsetype IN ('text','emoji','multchoice')),
    questionasked  VARCHAR(50) NOT NULL,
    PRIMARY KEY (responseid),
    FOREIGN KEY (feedbackid) REFERENCES feedback(feedbackid)
);

DROP TABLE IF EXISTS text_responses;
CREATE TABLE text_responses (
    responseid  INTEGER NOT NULL,
    txtmessage  VARCHAR(50) NOT NULL,
    PRIMARY KEY (responseid),
    FOREIGN KEY (responseid) REFERENCES responses(responseid)
);

DROP TABLE IF EXISTS emoji_responses;
CREATE TABLE emoji_responses (
    responseid  INTEGER NOT NULL,
    emojitype   VARCHAR(30) NOT NULL,
    PRIMARY KEY (responseid),
    FOREIGN KEY (responseid) REFERENCES responses(responseid)
);

DROP TABLE IF EXISTS mult_choice_responses;
CREATE TABLE mult_choice_responses (
    responseid      INTEGER NOT NULL,
    correctanswer   VARCHAR(10) NOT NULL,
    attendeeanswer  VARCHAR(10) NOT NULL,
    PRIMARY KEY (responseid),
    FOREIGN KEY (responseid) REFERENCES responses(responseid)
);