from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from  api.models import Track
import json

class Command(BaseCommand):
    help = 'Create tracks from a .json file'


    def handle(self, *args, **kwargs):
        # set path to the data file - tracks.json file
        data_file = settings.BASE_DIR/'data/tracks.json'
        assert data_file.exists()
        
        # load data file
        with open(data_file, 'r') as f:
            data = json.load(f)


        # create timezone-aware datetime object from JSON string
        DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
        for track in data:
            track_date = datetime.strptime(track['last_play'], DATE_FORMAT)
            track['last_play'] = make_aware(track_date)
        
        # convert a list of dictionaries to list of Track model and create all items using bulk_create()
        tracks = [Track(**track) for track in data]
        Track.objects.bulk_create(tracks)
