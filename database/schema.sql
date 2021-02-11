DROP TABLE hosts CASCADE;
CREATE TABLE hosts (
    hostid  INTEGER,
    PRIMARY KEY (hostid)
);

DROP TABLE meetings CASCADE;
CREATE TABLE meetings (
    meetingid  INTEGER
    title      VARCHAR(30) NOT NULL,
    runtime    TIME NOT NULL,
    PRIMARY KEY (meetingid)
);

DROP TABLE feedback CASCADE;
CREATE TABLE feedback (
    feedbackid    INTEGER,
    meetingid     INTEGER,
    userid        INTEGER NOT NULL,
    feedbacktype  VARCHAR(8) NOT NULL CHECK (feedbacktype IN ('Error','Question','Response','Mood')),
    PRIMARY KEY (feedbackid),
    FOREIGN KEY (meetingid)
);

DROP TABLE errors CASCADE;
CREATE TABLE errors (
    feedbackid  INTEGER,
    errortype   VARCHAR(10) NOT NULL,
    errmessage  VARCHAR(50) NOT NULL,
    PRIMARY KEY (feedbackid)
);

DROP TABLE questions CASCADE;
CREATE TABLE questions (
    feedbackid  INTEGER,
    qmessage    VARCHAR(50) NOT NULL,
    PRIMARY KEY (feedbackid)
);

DROP TABLE moods CASCADE;
CREATE TABLE moods (
    feedbackid  INTEGER,
    moodid      INTEGER,
    moodtype    VARCHAR(5) NOT NULL CHECK (moodtype IN ('Text','Emoji')),
    score       FLOAT NOT NULL,
    timeofmood  TIME NOT NULL,
    PRIMARY KEY (feedbackid),
    FOREIGN KEY (moodid)
);

DROP TABLE text_moods CASCADE;
CREATE TABLE text_moods (
    moodid      INTEGER,
    txtmessage  VARCHAR(50) NOT NULL,
    PRIMARY KEY (moodid),
);

DROP TABLE emoji_moods CASCADE;
CREATE TABLE emoji_moods (
    moodid     INTEGER,
    emojitype  VARCHAR(10) NOT NULL,
    PRIMARY KEY (moodid)
);

DROP TABLE responses CASCADE;
CREATE TABLE responses (
    feedbackid     INTEGER,
    responseid     INTEGER,
    responsetype   VARCHAR(10) NOT NULL CHECK (responsetype IN ('Text','Emoji','MultChoice')),
    questionasked  VARCHAR(50) NOT NULL,
    PRIMARY KEY (feedbackid),
    FOREIGN KEY (responseid)
);

DROP TABLE text_responses CASCADE;
CREATE TABLE text_responses (
    responseid  INTEGER,
    txtmessage  VARCHAR(50) NOT NULL,
    PRIMARY KEY (responseid)
);

DROP TABLE emoji_responses CASCADE;
CREATE TABLE emoji_responses (
    responseid  INTEGER,
    emojitype   VARCHAR(10) NOT NULL,
    PRIMARY KEY (responseid)
);

DROP TABLE mult_choice_responses CASCADE;
CREATE TABLE mult_choice_responses (
    responseid     INTEGER,
    correctanswer  VARCHAR(10) NOT NULL,
    useranswer     VARCHAR(10) NOT NULL,
    PRIMARY KEY (responseid)
);