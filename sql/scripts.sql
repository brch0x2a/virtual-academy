
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON * . * TO 'new_user'@'localhost';

FLUSH PRIVILEGES;

use academy;


drop table User_table;
drop table Lesson;
DROP TABLE Material;
drop table Module;
drop table Course;
drop table Category_course;
drop table Branch_of_knowledge;
drop table Enrollment;

create table User_table(
    id int not null AUTO_INCREMENT PRIMARY KEY,

    fname varchar(25),
    lname varchar(25),
    phone int,
    email varchar(120),
    identification_id varchar(50),
    password(256),
    card_number varchar(100)
);

create table Branch_of_knowledge(
    id int not null AUTO_INCREMENT PRIMARY KEY,
	name  varchar(50),
    image varchar(250)
) ;

create table Category_course(
	id int not null AUTO_INCREMENT PRIMARY KEY,
	name  varchar(50),
        
	id_branch int not null,
	FOREIGN key fk_id_branchfromBranch_of_knowledge(id_branch)
	REFERENCES Branch_of_knowledge(id)
	on DELETE RESTRICT
	on UPDATE CASCADE
);

create table Course(
	id int not null AUTO_INCREMENT PRIMARY KEY,
    
	id_category int not null,
	FOREIGN key fk_id_category_fromCourse(id_category)
	REFERENCES Category_course(id)
	on DELETE RESTRICT
	on UPDATE CASCADE,

    
	title varchar(60),

    image varchar(250), 
    
    description varchar(250),
    requirement varchar(100)
);

create table Module(
	id int not null AUTO_INCREMENT PRIMARY KEY,
	
    id_course int not null,
	FOREIGN key fk_id_course_fromCourse(id_course)
	REFERENCES Course(id)
	on DELETE RESTRICT
	on UPDATE CASCADE,
    
    title varchar(60),
    
    price float
);

CREATE TABLE Lesson (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title varchar(60),
    id_module INT NOT NULL,
    FOREIGN KEY fk_id_module_fromCourse(id_module)
        REFERENCES Module (id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    filepath VARCHAR(250)
);

CREATE table Enrollment(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,

    id_course INT NOT NULL,
    FOREIGN KEY fk_id_course_fromCourse(id_course)
        REFERENCES Course (id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    
    id_user INT NOT NULL,
    FOREIGN KEY fk_id_user_fromUser_table(id_user)
        REFERENCES User_table (id)
        ON DELETE RESTRICT ON UPDATE CASCADE,

    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

