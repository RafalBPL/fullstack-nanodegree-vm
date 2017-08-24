#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import math


def connect():
   """Connect to the PostgreSQL database.  Returns a database connection."""
   return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM matches;")
    conn.commit()
    c.close()
    
def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM players;")
    conn.commit()
    conn.close()
#deletePlayers()
def deleteScore():
    """Remove all the score records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM score;")
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM players;")
    count = c.fetchall()
    c.close()
    return count[0][0]

    
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s);", (name, ))
    conn.commit()
    conn.close()

#registerPlayer('rafal')

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
    deleteScore()
    conn = connect()
    c = conn.cursor()
    c.execute("""SELECT players.id, players.name, 
              COUNT(CASE players.id WHEN win THEN 1 ELSE NULL END) AS wins, 
              COUNT(matches.win) AS matches
              FROM players 
              LEFT JOIN matches ON players.id IN (win, loss)
              GROUP BY  players.id, name
              ORDER BY wins DESC;
              """)
    info = c.fetchall()
    """ Add total number of wins and total number of matches into table"""
    for player in info:
        c.execute("""INSERT INTO score (id, tot_win, tot_matches)
                     VALUES(%s, %s, %s)""",(player[0], player[2], player[3], ))
        conn.commit()
    c.close()
    return info

#print(playerStandings())


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    c.execute("""SELECT COUNT(*) FROM matches WHERE win = (%s) OR loss = (%s);""", (winner,winner))
    win = c.fetchall()
    
    game = win[0][0]    
    c.execute("""INSERT INTO matches (game,win, loss) 
                  VALUES ((%s),(%s),(%s)) 
                  """, (game ,winner, loser))
    conn.commit()
    c.close()
    return(win)

#print(reportMatch(105,106))

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
    # first update player stats 
    playerStandings()
    conn = connect()
    c = conn.cursor()
    c.execute("""SELECT score.id, players.name FROM score, players 
                  WHERE players.id = score.id 
                  ORDER BY tot_win;""")

    playerScore = c.fetchall()
    # players play in one match
    n = 2
    game = [playerScore[i:i+n] for i in range(0, len(playerScore), n)]
    
    # make final pairs
    finalPairs = [game[i][0] + game[i][1] for i in range(len(game))]
    
    return finalPairs
        
#print(swissPairings())

