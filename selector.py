from __future__ import print_function
from datetime import date
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import csv
import random


numberselector = {
    0: 1,  # 1 exercise from group A
    1: 2,  # 2 exercises from group B
    2: 2,  # 2 exercises from group C
    3: 3,  # 3 exercises from group D
    4: False  # a random number of exercises for group E
}

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))


def getWorkout():
    with open('Workout List.csv', 'r') as file:  # open file
        csvfile = csv.reader(file)  # parse csv as arrays
        result = ''
        lineNumber = 0  # track line numbers
        for line in csvfile:
            line = list(filter(None, line))  # remove white space
            totalSelections = numberselector.get(lineNumber)  # get number of lines from numberselector
            if (totalSelections):  # if numberselector has a number, pick that many exercises
                result = result + line[0] + ": " + ', '.join(random.sample(line[1:], totalSelections)) + '\n'
            else:  # if number selector does not have a number, pick 4-6 exercises
                result = result + line[0] + ": " + ', '.join(random.sample(line[1:], random.randrange(4, 6))) + '\n'
            lineNumber += 1  # add to lineNumber to start next Line
        print(result)
        return result


# Create new calendar
calendar = {
    'summary': 'Workout Schedule',
    'timeZone': 'America/New_York'
}

created_calendar = service.calendars().insert(body=calendar).execute()
print('Created calendar: ' + calendar['summary'])
today = date.today()
date = date.today()
while date.year == today.year:  # iterate until the current year is over
    if date.weekday() in [0, 2, 4]:  # check if date is monday, wednesday, or friday
        event = {
            'summary': 'Workout',
            'description': getWorkout(),
            'start': {
                'date': str(date),
                'timeZone': 'America/New_York',
            },
            'end': {
                'date': str(date),
                'timeZone': 'America/New_York',
            }
        }
        print(str(date))
        event = service.events().insert(calendarId=created_calendar['id'], body=event).execute()
        print('Event created: ' + (event.get('htmlLink')))
    date = date + timedelta(days=1)