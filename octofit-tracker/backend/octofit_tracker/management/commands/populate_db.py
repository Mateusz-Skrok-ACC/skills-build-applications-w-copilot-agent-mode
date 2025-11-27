
from django.core.management.base import BaseCommand
from django.conf import settings
import pymongo

# Sample data for superheroes and teams
USERS = [
    {"name": "Tony Stark", "email": "tony@marvel.com", "team": "Marvel"},
    {"name": "Steve Rogers", "email": "steve@marvel.com", "team": "Marvel"},
    {"name": "Bruce Wayne", "email": "bruce@dc.com", "team": "DC"},
    {"name": "Clark Kent", "email": "clark@dc.com", "team": "DC"},
]

TEAMS = [
    {"name": "Marvel", "members": ["tony@marvel.com", "steve@marvel.com"]},
    {"name": "DC", "members": ["bruce@dc.com", "clark@dc.com"]},
]

ACTIVITIES = [
    {"user_email": "tony@marvel.com", "activity": "Running", "duration": 30},
    {"user_email": "steve@marvel.com", "activity": "Cycling", "duration": 45},
    {"user_email": "bruce@dc.com", "activity": "Swimming", "duration": 25},
    {"user_email": "clark@dc.com", "activity": "Flying", "duration": 60},
]

LEADERBOARD = [
    {"team": "Marvel", "points": 150},
    {"team": "DC", "points": 120},
]

WORKOUTS = [
    {"name": "Super Strength", "description": "Strength training for superheroes."},
    {"name": "Flight Training", "description": "Aerobic workout for flying heroes."},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
