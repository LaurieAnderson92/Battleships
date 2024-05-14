# Fullstack Battleships

This apication is a simple battleships game played on a 5x5 grid, i chose this project to try and best understand the core mechanics of pythin and to gain experience with game design.

https://fullstack-battleships-4cdb574b78af.herokuapp.com/

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

### Initial Description

Welcome to the Battleship Game This is an interactive version of the classic board game, designed to be played directly within a command line terminal. Dive in to challenge your skills against the computer.

**Interactive Gameplay:** Input your cordinates and try to find the enemy ships, like the classic game 
**Dynamic Board:** New positions for yourelf and the enemy for every game.
**Color display:** using bthe dependency Colorama,the application can display colour into the command line.

## Design

### Description

They key part of the design is the gamplay loop that takes the players cordinates and the enemy's cordinates, checks them and then checks for a win/loose/draw situation.

In a tradional game of battleships, the player who has the first move has an advantage, the smaller the battle map the bigger the advante, as i decided to do a small game of 5x5 having the program allow the enemy to return fire before checking for victory allowed for an even game, with an even number of shots on both sides, and the potential for a draw.

### Flowchart

[Flowchart](assets/documentation/flowchart.png)

## Features

### Future Implementations

- A way for the player to place the position of their own ships
- A way to change the gridsize of the game before it starts
- Logic to implement having ships of greater sized of 1x1
- A way to restrat your game mid game
- A auto restart once you finish your game.

## Technologies Used

- Colorama to apply colour to the terminal text
- Heroku for hosting the application on a site

### Languages Used

- Python

### Frameworks, Libraries & Programs Used

- Colorama
- Git
- Github
- Gitpod
- Heroku

## Deployment & Local Development

### Deployment

Include instructions here on how to deploy your project. For your first project you will most likely be using GitHub Pages.

### Local Development

The local development section gives instructions on how someone else could make a copy of your project to play with on their local machine. This section will get more complex in the later projects, and can be a great reference to yourself if you forget how to do this.

#### How to Fork

Place instructions on how to fork your project here.

#### How to Clone

Place instructions on how to clone your project here.

## Testing

Testing was carried out during the creation of the progam and after when I opened it up to my friends and coleages to review, details of the test and the bugs found have been detailed below

### Tests

- Took turns firing missiles at the opponent's ships. using injected print statements to ensure hits are detected correctly and that the game state updates accordingly.

### Bugs & Fixes

- Bug: Name has no validation on the limit, which means a name of endless characters could be implemented.
- Fix:
- Status: Pending

- Bug: Unclear that it's five 1x1 ships on the grid
- Fix: 
- Status: Pending

- Bug: if multiple invalid inputs are placed, the battle grid goes out of view of the heroku terminal
- Fix:
- Status: Pending

## Credits

- My best friend [Jordan Cook](https://github.com/Bowtie7114), for helping me with my Imposter syndrome and giving me the last push I needed.
- My mentor [Rory Patrick Sheridan](https://github.com/Ri-Dearg), for his continued and invaluable help and insight.