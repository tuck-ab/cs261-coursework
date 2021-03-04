-- password: haskell
INSERT INTO hosts VALUES(1,"michael","0a9c51b61e2b775a59ee4773ff59f926641dd3392468fcec35c0ad2f29671b51","abb76399ad73c33e4eddaa2fd24537562299f8c7b9612972d3a207d825e66099");
-- password: deadlock
INSERT INTO hosts VALUES(2,"arpan","64a5db987724b7c1e7d2f0be64c39dd824665e41132846605e6bdb0ae211e8fb","9669f38c5547351b67ec7879bdcb5a5c57f9769c48938d36ac603beef57f96cd");
-- password: agents
INSERT INTO hosts VALUES(3,"james","a54593ba507d58f75da7e58927774b1aaecb49b9ec74cf31636d53ee56a91111","1543e6382f6c2c2ba3293b168367488989ede6e43eba7294c0281960d46d68bf");
-- password: asymptotic
INSERT INTO hosts VALUES(4,"marcin","5f51b147a9af7c0a0e0a0fa7c5b42d610825dbb35aa03139239d3d65fb37b0ed","bf49118a49f5fc7acf71215cbbe6ffc4b085e78b59050a0ff22fa3a12170b56a");

INSERT INTO meetings VALUES(1111,1,"Functional Programming","1:00:00","2021-03-01 16:35:05");
INSERT INTO meetings VALUES(2222,2,"Operating Systems and Computer Networks","0:58:00","2021-02-25 15:12:07");
INSERT INTO meetings VALUES(3333,3,"Artificial Intelligence","0:55:00","2021-01-08 09:01:45");
INSERT INTO meetings VALUES(4444,4,"Algorithms","0:45:00","2021-02-14 12:54:09");

INSERT INTO feedback VALUES(1,1,"error");
INSERT INTO feedback VALUES(2,1,"question");
INSERT INTO feedback VALUES(3,1,"mood");
INSERT INTO feedback VALUES(4,1,"response");
INSERT INTO feedback VALUES(5,2,"error");
INSERT INTO feedback VALUES(6,2,"question");
INSERT INTO feedback VALUES(7,2,"mood");
INSERT INTO feedback VALUES(8,2,"response");
INSERT INTO feedback VALUES(9,3,"error");
INSERT INTO feedback VALUES(10,3,"question");
INSERT INTO feedback VALUES(11,3,"mood");
INSERT INTO feedback VALUES(12,3,"response");
INSERT INTO feedback VALUES(13,4,"error");
INSERT INTO feedback VALUES(14,4,"question");
INSERT INTO feedback VALUES(15,4,"mood");
INSERT INTO feedback VALUES(16,4,"response");

INSERT INTO errors VALUES(1,"audio","We can't hear you");
INSERT INTO errors VALUES(5,"video","Screen not visible");
INSERT INTO errors VALUES(9,"audio","Microphone not turned on");
INSERT INTO errors VALUES(13,"video","Very pixelated and laggy");

INSERT INTO questions VALUES(2,"What is a monad?");
INSERT INTO questions VALUES(6,"How do I implement multithreading?");
INSERT INTO questions VALUES(10,"When should I backtrack in a search?");
INSERT INTO questions VALUES(14,"Why is dynamic programming efficient?");

INSERT INTO moods VALUES(1,3,"text",3,30);
INSERT INTO moods VALUES(2,7,"emoji",2,12);
INSERT INTO moods VALUES(3,11,"text",4,25);
INSERT INTO moods VALUES(4,15,"emoji",-1,44);

INSERT INTO text_moods VALUES(1,"This lecture is going very well, good job!");
INSERT INTO text_moods VALUES(3,"I can't believe how absolutely amazing this event is. I love it!");

INSERT INTO emoji_moods VALUES(2,":smile:");
INSERT INTO emoji_moods VALUES(4,":angry:");

INSERT INTO responses VALUES(1,4,"text","Express f = \x -> \y -> x * y using syntactic sugar");
INSERT INTO responses VALUES(2,8,"emoji","How comfortable are you with mutex locks?");
INSERT INTO responses VALUES(3,12,"multchoice","True or False: A rational agent is successful all of the time");
INSERT INTO responses VALUES(4,16,"text","What is the asymptotic running time of the early-finish-time first algorithm?");

INSERT INTO text_responses VALUES(1,"f x y = x * y");
INSERT INTO text_responses VALUES(4,"O(nlogn)");

INSERT INTO emoji_responses VALUES(2,":thumbsup:");

INSERT INTO mult_choice_responses VALUES(3,"True");