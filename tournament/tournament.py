#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    #Connecct to database
    db = connect()
    cur = db.cursor()
    #Database execution
    cur.execute("DELETE FROM MATCH;")
    db.commit()
    cur.close()
    db.close()
    return 


def deletePlayers():
    """Remove all the player records from the database."""
    #Connecct to database
    db = connect()
    cur = db.cursor()
    #Database execution
    cur.execute("DELETE FROM PLAYER;")
    db.commit()
    #Close database connection
    cur.close()
    db.close()
    return 

def countPlayers():
    """Returns the number of players currently registered."""
    #Connecct to database
    db = connect()
    cur = db.cursor()
    #Database execution
    cur.execute("SELECT COUNT(*) FROM PLAYER;")
    result = cur.fetchone()
    #Close database connection
    cur.close()
    db.close()
    return result[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    #Connecct to database
    db = connect()
    cur = db.cursor()
    #Database execution
    SQL = "INSERT INTO PLAYER (NAME) VALUES (%s);"
    data = (name, )
    cur.execute(SQL, data)
    db.commit()
    #Close database connection
    cur.close()
    db.close()

    return


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

    #Connecct to database
    db = connect()
    cur = db.cursor()
    #Database execution
    SQL = """SELECT PLAYER.ID, PLAYER.NAME, COALESCE(SUM(CASE WHEN PLAYER.ID = MATCH.WINNER THEN 1 ELSE 0 END), 0) AS WINS, COUNT(MATCH.ID) 
    FROM PLAYER LEFT OUTER JOIN MATCH ON (PLAYER.ID = MATCH.WINNER OR PLAYER.ID = MATCH.LOSER)
    GROUP BY PLAYER.ID ORDER BY WINS;"""
    cur.execute(SQL)    
    results = cur.fetchall()
    #Close database connection
    cur.close()
    db.close()
    return results

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    #Connecct to database
    db = connect()
    cur = db.cursor()
    #Database execution
    SQL = "INSERT INTO MATCH (WINNER, LOSER) VALUES (%s, %s);"
    data = (winner, loser, )
    cur.execute(SQL, data)
    db.commit()
    #Close database connection
    cur.close()
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
    #Creates an empty list and tuple
    swisslist = []
    temptuple = ()
    #
    count = 0
    players = playerStandings()
    #Go through each player record and add every pair together as a tuple
    for p in players:
        if count % 2 == 0: 
            temptuple += (p[0], p[1])
        else:
            temptuple += (p[0], p[1])
            #takes paried tuple and appends to output list
            swisslist.append(temptuple)
            temptuple = ()
        #Increase count by one to match every 2 players
        count += 1
    return swisslist