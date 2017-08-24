-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

\c tournament

CREATE TABLE players (
    id serial UNIQUE PRIMARY KEY,
    name VARCHAR(90) );

CREATE TABLE matches(
    game INTEGER NOT NULL,
    win INTEGER REFERENCES players(id) ON DELETE CASCADE,
    loss INTEGER REFERENCES players(id) ON DELETE CASCADE
    );
    
CREATE TABLE score (
    id serial REFERENCES players(id) ON DELETE CASCADE,
    tot_win INTEGER,
    tot_matches INTEGER)
