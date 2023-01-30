drop table grijeh;
create database grijeh;
use grijeh;

drop table grijesi;
CREATE TABLE grijesi(
    id INTEGER PRIMARY KEY,
    naziv VARCHAR(60) NOT NULL,
	username VARCHAR(60) NOT NULL,
    grijesi VARCHAR(60) NOT NULL
    
);

drop table login;
CREATE table login (
    id INTEGER PRIMARY KEY,
    username VARCHAR(60) NOT NULL,
    passwordd VARCHAR(60) NOT NULL
);

drop trigger kriptiranje;

DELIMITER //
CREATE TRIGGER kriptiranje
 BEFORE INSERT ON login
 FOR EACH ROW
BEGIN
 INSERT INTO login VALUES (new.id,new.username,md5(new.passwordd));

END//
DELIMITER ;

insert into grijesi values ( 1 ,"test","test","kuis");
insert into login values ( 1 ,"test","test");
insert into login values ( 2,"test","test");
insert into login values ( 3 ,"test","test");

select * from login;
select * from grijesi;

select max(id) from login;
