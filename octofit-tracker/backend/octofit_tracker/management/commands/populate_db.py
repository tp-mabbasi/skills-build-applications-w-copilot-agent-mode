
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **options):
        # Use PyMongo to drop collections directly to avoid Djongo ORM issues
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        for collection in ['activity', 'leaderboard', 'workout', 'user', 'team']:
            db[collection].drop()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel')
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel')
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc')
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc')

        # Create Activities
        Activity.objects.create(user=tony, activity_type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, activity_type='swim', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='yoga', duration=20, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, points=120)
        Leaderboard.objects.create(user=steve, points=110)
        Leaderboard.objects.create(user=bruce, points=130)
        Leaderboard.objects.create(user=clark, points=125)

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
