#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament

import psycopg2
import random


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        cursor = psycopg2.connect("dbname={}".format(database_name))
        db = cursor.cursor()
        return cursor, db
    except:
        print("<error message>")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    query = "TRUNCATE matches"
    cursor.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    query = "TRUNCATE players CASCADE"
    cursor.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    query = "SELECT count(id) AS num FROM players"
    cursor.execute(query)
    testCount = cursor.fetchone()
    db.commit()
    db.close()
    return testCount[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    query = "INSERT INTO players (name) VALUES (%s)"
    parameter = (name,)
    cursor.execute(query, parameter)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    query = "SELECT * from player_standings"
    cursor.execute(query)
    result = cursor.fetchall()
    db.commit()
    db.close()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s)"
    parameter = (winner, loser)
    cursor.execute(query, parameter)
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    db, cursor = connect()
    cursor.execute("SELECT * FROM player_standings ORDER BY wins DESC")
    player_list = cursor.fetchall()

    i = 0
    pairings = []
    while i < len(player_list):
        id1 = player_list[i][0]
        name1 = player_list[i][1]
        id2 = player_list[i + 1][0]
        name2 = player_list[i + 1][1]
        pairings.append((id1, name2, id2, name2))
        i = i + 2

    return pairings
