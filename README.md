# Lotto 6 of 49

Lotto 6/49 is a popular lottery game played in many countries around the world. The "6/49" in its name refers to the format of the game, where players must choose 6 numbers out of a pool of 49 numbers. Our game has the posibility to play SinglePlayer aswell as Multiplayer with your friends.
![alt Lotto 6 of 49 game shown as Singleplayer](./assets/images/First%20impression.png)


## Features

### Existing Features

- The Game Mode selection input
    - This will allow the user to select the game mode, Singleplayer to play the game by himself or herself, the ability to enter a number of players for Multiplayer option, or simply just to Quit.
- The Number Selection
    - In this part, the game will run for 2 players. Every Player will chose a number between 1 and 49, the numbers cannot be the same, and must be between 1 and 49. After the players will type the 6 numbers they will be messaged that " Player x has finished entering the numbers".
    - ![alt Player number selection section](./assets/images/number%20selection.png)
- The Result Area
    - Firstly the "winning numbers" will be shown and then, it will display a message for each user, of how many numbers each one got right.
    - ![alt Result area with every player right number count](./assets/images/Result%20area.png)

### Features left to implement

- Adding the number of games won for every player


## Testing

### Validator Testing

- No errors were returned from [Pep8 Validator](https://pep8ci.herokuapp.com/#)

### Unfixed Bugs

There are no existing bugs that developer knows about, after testing in the pep8 validator and multiple times testing the app.

## Deployment

- This app was deployed to Heroku App. Steps:
    - In the heroku panel, click new
    - Deplyment method via GitHub
    - Connect your project repository with Heroku
    - Go to Settings:
        - Click on Reveal config Vars
        - KEY is PORT and VALUE is 8000
        - Click on Add buildpack and install python and nodejs
    - From Manual Deploy, select main branch

## Credits

- [W3 Schools](www.w3schools.com)
- [Geek for Geeks](www.geeksforgeeks.org)