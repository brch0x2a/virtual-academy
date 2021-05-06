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


use academy;

create table Category_course(
	id int not null AUTO_INCREMENT PRIMARY KEY,
	name  varchar(50)
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

CREATE TABLE Material (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title varchar(60),
    id_module INT NOT NULL,
    FOREIGN KEY fk_id_module_fromCourse(id_module)
        REFERENCES Module (id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    filepath VARCHAR(250)
);



