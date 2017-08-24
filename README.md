# Project Description: Tournament Planner

  In this project, you’ll be writing a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.
  
  The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

  This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

## Code Templates
The templates for this project are in the <b> tournament </b>  subdirectory of your VM’s <b> /vagrant </b> directory. You’ll find three files there: <b> tournament.sql </b>, <b> tournament.py </b>, and <b> tournament_test.py </b>.

The template file <b> tournament.sql </b> is where you will put the database schema, in the form of SQL  <b> create table </b> commands. Give your tables names that make sense to you, and give the columns descriptive names. You'll also need to create the database itself; see below.

The template file <b> tournament.py </b> is where you will put the code of your module. In this file you’ll see stubs of several functions. Each function has a docstring that says what it should do.

Finally, the file <b> tournament_test.py </b> contains unit tests that will test the functions you’ve written in <b> tournament.py </b> . You can run the tests from the command line, using the command <b> python tournament_test.py </b>.

## Creating Your Database
Before you can run your code or create your tables, you'll need to use the <b> create database </b> command in <b> psql </b> to create the database. Use the name <b> tournament </b> for your database.

Then you can connect <b> psql </b> to your new database and create your tables from the statements you've written in <b> tournament.sql </b> . You can do this in either of two ways:

  1.Paste each statement in to <b> psql </b>.
  2.Use the command <b> \i tournament.sql </b> to import the whole file into <b> psql </b> at once.
  
Remember, if you get your database into a bad state you can always <b> drop </b> tables or the whole database to clear it out.

## Design Notes
Rely on the unit tests as you write your code. If you implement the functions in the order they appear in the file, the test suite can give you incremental progress information.

The goal of the Swiss pairings system is to pair each player with an opponent who has won the same number of matches, or as close as possible.

You can assume that the number of players in a tournament is an even number. This means that no player will be left out of a round.

Your code and database only needs to support a single tournament at a time. All players who are in the database will participate in the tournament, and when you want to run a new tournament, all the game records from the previous tournament will need to be deleted. In one of the extra-credit options for this project, you can extend this program to support multiple tournaments.

## Functions in tournament.py

### registerPlayer(name)
Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

### countPlayers()
Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

### deletePlayers()
Clear out all the player records from the database.

### reportMatch(winner, loser)
Stores the outcome of a single match between two players in the database.

### deleteMatches()
Clear out all the match records from the database.

### deleteScore():
Remove all the score records from the database.

#### playerStandings()
Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

### swissPairings()
Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.


## Getting started guide -

https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true
