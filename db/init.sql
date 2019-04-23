CREATE DATABASE my_new_database;

USE my_new_database;

CREATE TABLE Restos(
   id INT,
   rname VARCHAR(60),
   PRIMARY KEY ( id )
);

CREATE TABLE Tables(
   id INT,
   resto_id INT,
   max_people INT,
   PRIMARY KEY ( id ),
   FOREIGN KEY ( resto_id )
        REFERENCES Restos(id)
);

CREATE TABLE Bookings(
   id INT,
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

INSERT INTO Restos (id, rname) VALUES (0, "Maria si Ion");
INSERT INTO Restos (id, rname) VALUES (1, "Roxy Pub");
INSERT INTO Restos (id, rname) VALUES (2, "Pub 18");

INSERT INTO Tables (id, resto_id, max_people) VALUES (0, 0, 5);
INSERT INTO Tables (id, resto_id, max_people) VALUES (1, 0, 2);
INSERT INTO Tables (id, resto_id, max_people) VALUES (2, 0, 8);


INSERT INTO Tables (id, resto_id, max_people) VALUES (0, 1, 1);
INSERT INTO Tables (id, resto_id, max_people) VALUES (1, 1, 2);
INSERT INTO Tables (id, resto_id, max_people) VALUES (2, 1, 3);
INSERT INTO Tables (id, resto_id, max_people) VALUES (1, 1, 4);
INSERT INTO Tables (id, resto_id, max_people) VALUES (2, 1, 5);


INSERT INTO Tables (id, resto_id, max_people) VALUES (0, 2, 3);
INSERT INTO Tables (id, resto_id, max_people) VALUES (1, 2, 3);
INSERT INTO Tables (id, resto_id, max_people) VALUES (2, 2, 3);
INSERT INTO Tables (id, resto_id, max_people) VALUES (0, 2, 3);