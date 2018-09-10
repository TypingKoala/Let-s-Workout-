# Let's Workout!
Let's Workout is an app that imports a comma-separated values file of workouts and generates a workout calendar for the year.

## Functionality
This app generates randomized workouts and adds it to your Google Calendar, allowing you to be more motivated to switch up your routine.

When you import a list of workouts separated into groups, you are able to set how many workouts per group you would like on a workout day. You are also able to select what workout days you would like every week. For example:


Workout Days: Mon, Wed, Fri, Sat
Workout Groups: 4 workouts from Group A, 2 workouts from Group B, 3 workouts from Group C, a random number of workouts from Group D

## Usage
1. Install the Google Calendar Client Library via pip:
   `pip install --upgrade google-api-python-client oauth2client`
2. [Create a credentials.json file](https://developers.google.com/calendar/quickstart/python#step_1_turn_on_the) with access to the Google Calendar API, and place it into the project directory
3. Run selector.py using python `python selector.py`.
4. Follow the OAuth authentication steps and watch the magic unfold upon a new calendar.