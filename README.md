# HYBRD * Hybrid Athlete Training Planner

## Description

HYBRD is a fitness planning application designed for hybrid athletes training across multiple disciplines including running, cycling, swimming, and triathlon events. 
The app collects information about a user’s current fitness level, race goals, weekly training availability, and personal best performances to automatically generate
a structured training plan.

The project was built as a personal software development project to improve my programming skills outside of university while also applying real*world problem-solving
and UI design concepts.

## Why I Built This

After graduating from university, I wanted to continue developing my software engineering skills through a larger personal project that combined both backend logic
and frontend application development and also one of my interests which is sport.

As someone interested in endurance sports and hybrid training, I thought building a training planner similar to apps like Runna would be both technically challenging
and personally interesting. I wanted to create something that could dynamically generate training plans based on user input rather than just displaying static
information.

The project also allowed me to improve my understanding of:
* Object-oriented programming
* UI development
* Data structures and algorithms
* Application flow and state management
* Software architecture and planning

## Features

* Multi*sport athlete support:
  * Running
  * Cycling
  * Swimming
  * Triathlon

* Race selection system
  * Running distances
  * Cycling distances
  * Swimming distances
  * Ironman events

* User fitness profiling
  * Longest effort
  * Weekly training volume
  * Personal best times
  * Training availability

* Dynamic plan generation
  * Easy runs
  * Tempo sessions
  * Interval sessions
  * Long runs
  * Rest days

* Interactive UI built with Kivy
* Scrollable mobile-style screens
* Training day selection system
* Long run day selection dropdown

## Tech Stack

* Python
* Kivy (Frontend/UI Framework)
* PyCharm
* Git & GitHub
* GitHub Actions (CI)
* pytest (Testing)
* Flake8 (Code Quality)

Concepts used:
* Object*Oriented Programming
* Dictionaries and nested data structures
* Event-driven programming
* Screen management/navigation
* Dynamic workout generation

## Software Development

* Continuous Integration (CI) using GitHub Actions
* Automated testing using pytest
* Automated code quality checks using Flake8
* Git and GitHub version control

## How It Works

1. The user selects which sports they participate in.
2. The app asks for race goals and target events.
3. The user enters current fitness information:
   * Longest distance
   * Weekly volume
   * PB times
4. The user selects:
   * Available training days
   * Long Distance Day
   * Number of weekly sessions
   * Plan length
5. The application generates a structured weekly training schedule using dictionaries and workout rotation logic including planned distances.

## Recent Screenshots
Intro Screen:

<img width="788" height="931" alt="image" src="https://github.com/user*attachments/assets/993554a1*3e33*4ab9*9828*c9b6ffec43b6" />

Select Race Screen:

<img width="793" height="931" alt="image" src="https://github.com/user*attachments/assets/f8d498b1*9973*41dc*97a0*61256ca6bff6" />
<img width="778" height="744" alt="image" src="https://github.com/user*attachments/assets/f2d8e169*0a07*4a8e*b185*14ad467c7a0a" />

Running Profile Screen:

<img width="788" height="934" alt="image" src="https://github.com/user*attachments/assets/22f256ad*a153*4615*a031*a72af662c68e" />

Race PBs Screen:

<img width="792" height="929" alt="image" src="https://github.com/user*attachments/assets/a890b216*394b*4b3b*929a*9abfe8c36dfc" />

Runner Level Screen:

<img width="791" height="766" alt="image" src="https://github.com/user*attachments/assets/77b105bc*2241*4917*ba3e*ac6c76e53872" />

Build Plan Screen:

<img width="792" height="936" alt="image" src="https://github.com/user*attachments/assets/b32ec87c*61ad*4a3f*b4a9*670d211d75fc" />

Plan Screen:

<img width="780" height="763" alt="image" src="https://github.com/user*attachments/assets/20df9f18*3847*4cae*94a9*90debeb15c45" />
<img width="798" height="764" alt="image" src="https://github.com/user*attachments/assets/2e912d72*9999*4fe1*9686*85c06b718164" />
<img width="798" height="751" alt="image" src="https://github.com/user*attachments/assets/8d901ddf*78c2*4e68*874d*54a8581d0c1a" />
<img width="801" height="760" alt="image" src="https://github.com/user*attachments/assets/2ebb6dfe*1405*45da*b135*803caa6ee4e9" />
<img width="796" height="759" alt="image" src="https://github.com/user*attachments/assets/8450a79a*3b16*46e1*9844*91f1b1fad6d3" />
<img width="796" height="452" alt="image" src="https://github.com/user*attachments/assets/0a3a819f*73c3*44bb*a566*aa9aff461d77" />


## Current imminent  Improvements
* Final Week Distance Calculation correction
* Include Taper Weeks leading up to race to get the user ready for race day.
* Improve long run and easy run creation to really bring that side of the plan to life.
* Correct Build Plan Screen PB Time from seconds to an actual time.
* More appealing Build Plan Screen

## Future Improvements 
* Export training plans to PDF
* Save user accounts and plans
* Mobile deployment
* Improved UI styling and animations
* Calendar integration
* Heart rate zone calculations
* AI-generated workout recommendations
* Strength training integration
* Progress tracking and analytics
  
## What I Learned

Through this project I improved my understanding of:

* Python application structure
* Frontend development using Kivy
* Managing data across multiple screens
* Event-driven programming
* Building dynamic algorithms
* Creating reusable UI components
* Structuring larger software projects
* Using Git and GitHub for version control

I also learned the importance of planning software architecture early, especially when managing multiple screens, user inputs, and dynamically generated data.
