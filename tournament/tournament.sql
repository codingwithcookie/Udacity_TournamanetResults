-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament

CREATE TABLE PLAYER(
   ID SERIAL PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL
);

CREATE TABLE MATCH(
	ID SERIAL PRIMARY KEY NOT NULL,
	WINNER INT REFERENCES PLAYER(ID) NOT NULL,
	LOSER INT REFERENCES PLAYER(ID) NOT NULL
	);



