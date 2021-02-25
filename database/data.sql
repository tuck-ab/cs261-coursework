INSERT INTO hosts VALUES(1);
INSERT INTO hosts VALUES(2);
INSERT INTO hosts VALUES(3);

INSERT INTO meetings VALUES(1,1,"Functional Programming",60);
INSERT INTO meetings VALUES(2,1,"Operating Systems and Computer Networks",58);
INSERT INTO meetings VALUES(3,2,"Artificial Intelligence",55);
INSERT INTO meetings VALUES(4,3,"Algorithms",45);

INSERT INTO attendees VALUES(1,1);
INSERT INTO attendees VALUES(2,1);
INSERT INTO attendees VALUES(3,1);
INSERT INTO attendees VALUES(4,1);
INSERT INTO attendees VALUES(1,2);
INSERT INTO attendees VALUES(2,2);
INSERT INTO attendees VALUES(3,2);
INSERT INTO attendees VALUES(4,2);
INSERT INTO attendees VALUES(1,3);
INSERT INTO attendees VALUES(2,3);
INSERT INTO attendees VALUES(3,3);
INSERT INTO attendees VALUES(4,3);
INSERT INTO attendees VALUES(1,4);
INSERT INTO attendees VALUES(2,4);
INSERT INTO attendees VALUES(3,4);
INSERT INTO attendees VALUES(4,4);

INSERT INTO feedback VALUES(1,1,1,"error",1);
INSERT INTO feedback VALUES(2,1,2,"question",1);
INSERT INTO feedback VALUES(3,1,3,"mood",0);
INSERT INTO feedback VALUES(4,1,4,"response",0);
INSERT INTO feedback VALUES(5,2,1,"error",0);
INSERT INTO feedback VALUES(6,2,2,"question",0);
INSERT INTO feedback VALUES(7,2,3,"mood",1);
INSERT INTO feedback VALUES(8,2,4,"response",1);
INSERT INTO feedback VALUES(9,3,1,"error",1);
INSERT INTO feedback VALUES(10,3,2,"question",0);
INSERT INTO feedback VALUES(11,3,3,"mood",1);
INSERT INTO feedback VALUES(12,3,4,"response",0);
INSERT INTO feedback VALUES(13,4,1,"error",0);
INSERT INTO feedback VALUES(14,4,2,"question",1);
INSERT INTO feedback VALUES(15,4,3,"mood",0);
INSERT INTO feedback VALUES(16,4,4,"response",1);

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

INSERT INTO mult_choice_responses VALUES(3,"False","True");