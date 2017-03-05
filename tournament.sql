-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like

-- deletes database if this database exists
DROP DATABASE IF EXISTS tournament;

-- creates the database
CREATE DATABASE tournament;

-- connects to the database created
\c tournament

-- creates the table players
CREATE TABLE players (id SERIAL PRIMARY KEY, 
					  name TEXT);

-- players added into my players table
INSERT INTO players (name) VALUES ('Win');
INSERT INTO players (name) VALUES ('Minh');
INSERT INTO players (name) VALUES ('Tom');
INSERT INTO players (name) VALUES ('Vincent');
INSERT INTO players (name) VALUES ('Jon');
INSERT INTO players (name) VALUES ('Sandy');
INSERT INTO players (name) VALUES ('Zaira');
INSERT INTO players (name) VALUES ('Tammy');
INSERT INTO players (name) VALUES ('Ben');
INSERT INTO players (name) VALUES ('Liz');
INSERT INTO players (name) VALUES ('Amanda');
INSERT INTO players (name) VALUES ('Daisy');
INSERT INTO players (name) VALUES ('Thuy');
INSERT INTO players (name) VALUES ('Kim');
INSERT INTO players (name) VALUES ('Chris');
INSERT INTO players (name) VALUES ('Tam');
INSERT INTO players (name) VALUES ('Serg');

-- creates the matches table
create table matches (id SERIAL PRIMARY KEY, 
	winner INTEGER REFERENCES players(id), 
	loser INTEGER REFERENCES players(id));

-- creates a view for total matches played
CREATE VIEW matches_played AS
SELECT players.id, players.name, COUNT(players.id) AS played
    FROM players, matches
    WHERE players.id = matches.winner OR players.id = matches.loser
    GROUP BY id 
    ORDER BY played DESC;

-- number of wins view
CREATE VIEW win_total AS
	SELECT players.name, COUNT(players.name) AS win_total
	FROM matches, players
	WHERE players.id = matches.winner
  	GROUP BY players.name
  	ORDER BY win_total DESC;

-- creates a view for the player's standing
CREATE VIEW player_standings AS 
	select players.id, players.name, count(matches.winner) as wins, (select count(*) from matches where players.id = matches.winner or players.id = matches.loser) as match from players
	left join matches on players.id = matches.winner
	group by players.id
	order by wins desc;