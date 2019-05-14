CREATE DATABASE my_new_database;

USE my_new_database;

CREATE TABLE Restos(
   id INT AUTO_INCREMENT,
   rname VARCHAR(60),
   PRIMARY KEY ( id )
);

CREATE TABLE Tables(
   id INT AUTO_INCREMENT,
   resto_id INT,
   max_people INT,
   PRIMARY KEY ( id ),
   FOREIGN KEY ( resto_id )
        REFERENCES Restos(id)
);

CREATE TABLE Bookings(
   id INT AUTO_INCREMENT,
   resto_id INT,
   table_id INT,
   client_name VARCHAR(60),
   client_id VARCHAR(60),
   bdate VARCHAR(60),
   btime VARCHAR(60),
   PRIMARY KEY ( id ),
   FOREIGN KEY ( resto_id )
      REFERENCES Restos(id),
   FOREIGN KEY ( table_id )
      REFERENCES Tables(id)
);

INSERT INTO Restos (id, rname) VALUES (3, "Maria si Ion");
INSERT INTO Restos (id, rname) VALUES (1, "Roxy Pub");
INSERT INTO Restos (id, rname) VALUES (2, "Pub 18");

INSERT INTO Tables (id, resto_id, max_people) VALUES (3, 3, 5);
INSERT INTO Tables (id, resto_id, max_people) VALUES (1, 3, 2);
INSERT INTO Tables (id, resto_id, max_people) VALUES (2, 3, 8);


INSERT INTO Tables (id, resto_id, max_people) VALUES (6, 1, 1);
INSERT INTO Tables (id, resto_id, max_people) VALUES (7, 1, 2);
INSERT INTO Tables (id, resto_id, max_people) VALUES (8, 1, 3);
INSERT INTO Tables (id, resto_id, max_people) VALUES (4, 1, 4);
INSERT INTO Tables (id, resto_id, max_people) VALUES (5, 1, 5);


INSERT INTO Tables (id, resto_id, max_people) VALUES (9, 2, 3);
INSERT INTO Tables (id, resto_id, max_people) VALUES (10, 2, 3);
INSERT INTO Tables (id, resto_id, max_people) VALUES (11, 2, 3);
INSERT INTO Tables (id, resto_id, max_people) VALUES (12, 2, 3);
