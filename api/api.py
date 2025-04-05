from api.models import Track
from api.schemas import TrackSchema, TrackNotFoundSchema
from ninja import NinjaAPI
from typing import List, Optional


app = NinjaAPI()


@app.get('/tracks', response=List[TrackSchema])
def get_all_tracks(request, q: Optional[str] = None):
    if q:
        return 404, Track.objects.filter(title__icontains=q)
    return Track.objects.all()


@app.get('/tracks/{track_id}', response={200: TrackSchema, 404: TrackNotFoundSchema})
def get_track(request, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        return 200, track
    
    except Track.DoesNotExist as e:
        return 404, {'message': 'Track does not exist'}


@app.post('/track/create', response={201: TrackSchema})
def create_track(request, track: TrackSchema):
    track = Track.objects.create(**track.dict())
    return track


@app.put('/tracks/{track_id}', response={200: TrackSchema, 404: TrackNotFoundSchema})
def update_track(request, track_id: int, data: TrackSchema):
    try:
        track = Track.objects.get(pk=track_id)
        
        for attr, val in data.dict().items():
            setattr(track, attr, val)
        
        track.save()
        return 200, track
    
    except Track.DoesNotExist as e:
        return 404, {'message': 'Track does not exist'}


@app.delete('/tracks/{track_id}/delete', response={200: None, 404: TrackNotFoundSchema})
def delete_track(request, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        track.delete()
        return 200
    
    except Track.DoesNotExist as e:
        return 404, {'message': 'Track does not exist'}
