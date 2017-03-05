#Tournament Results

This project teaches you how to create, manipulate, and use databases through the modeling of a database schema. It is broken down into two parts: 

1. Modeling our database schema in *tournament.sql* where the SQL code will be created using the PostgreSQL datbase that will keep track of the players and matches in the game tournament. 

2. Writing and defining the python code in *tournament.py* that will keep track of the swiss tournament. 

The idea behind this database project on a swiss tournament is that we want our code to match players of the same or close to the number of wins a player has. Each player has a fair chance to play against different players of the same level in several different rounds and are not eliminated from play. The winner of the tournament will be the player that achieves the most wins.  

##Setup

This project requires a virtual machine such as VirtualBox and Vagrant. The virtual machine is preconfigured with a PostgreSQL database server.

Links to VirtualBox and Vagrant:
[Virtual Box](https://www.virtualbox.org/wiki/Downloads)
[Vagrant](https://www.vagrantup.com/)


###Run Project
* Clone or download and unzip this repo on your computer.
* Open Git Bash 
* Change directory to vagrant
* Run vagrant up (this will start a virtual machine)
* After vagrant is running, run vagrant ssh to log into the virtual machine

###Testing
To test out the files, type psql and add the path to *tournament.sql* in your virtual machine: 

$ psql -f tournament.sql (This will create the database schema for the Tournament).

For windows users, open a second window (Git Bash) to test *tournament_test.py*. To do this, type python tournament_test.py then press enter. Your test should look like this:

vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!



