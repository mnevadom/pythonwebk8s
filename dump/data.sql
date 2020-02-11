CREATE DATABASE pyapp;

CREATE TABLE Personas (
    PersonaID int,
    Nombre varchar(255),
    Apellido1 varchar(255)
);

INSERT INTO Personas(PersonaID,Nombre,Apellido1) VALUES (1,'Mario','Nevado');

INSERT INTO Personas(PersonaID,Nombre,Apellido1) VALUES (2,'Pablo','Chico');
