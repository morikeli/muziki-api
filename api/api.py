from api.models import Track
from api.schemas import TrackSchema, TrackNotFoundSchema
from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from typing import List, Optional


app = NinjaAPI()


@app.get('/tracks', response=List[TrackSchema])
def get_all_tracks(request, q: Optional[str] = None):
    """
    This is a router to get all tracks from the db.

    Args:
        request (_type_): django's request object.
        q (Optional[str], optional): Query track title containing the typed string or character. Defaults to None.

    Returns:
        404: if the queried track title does not match any track's title.
        track: All track records stored in the db or results of the track containing the queried string.
    """
    if q:
        return 404, Track.objects.filter(title__icontains=q)
    return Track.objects.all()


@app.get('/tracks/{track_id}', response={200: TrackSchema, 404: TrackNotFoundSchema})
def get_track(request, track_id: int):
    """
    This router returns a track that matches the provided track ID.

    Args:
        track_id (int): Track ID.

    Returns:
        200, track: Returns response data and http status code 200(OK) if the track is found
        404: if the track record is not found.
    """
    try:
        track = Track.objects.get(pk=track_id)
        return 200, track
    
    except Track.DoesNotExist as e:
        return 404, {'message': 'Track does not exist'}


@app.post('/track/create', response={201: TrackSchema})
def create_track(request, track: TrackSchema):
    """
    This router is used to create a new track record.

    Args:
        track (TrackSchema): schema is used to represent the response data format.

    Returns:
        201: return http status code 201 (CREATED) if the track was created successfully.
        track: response data of the created music track
    """
    track = Track.objects.create(**track.dict())
    return track


@app.put('/tracks/{track_id}', response={200: TrackSchema, 404: TrackNotFoundSchema})
def update_track(request, track_id: int, data: TrackSchema):
    """
    This router is used to update a single music track. The track's ID is used.

    Args:
        track_id (int): track ID
        data (TrackSchema): schema is used to represent the response data format.

    Returns:
        200, track: Returns response data and http status code 200(OK) if the track is found
        404: if the track record is not found.
    """
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
    """
    This router is used to delete a music track. The track ID is used to get the track.

    Args:
        track_id (int): track ID

    Returns:
        200: Returns http status code 200(OK) if the track is deleted successfully.
        404: if the track record is not found.
    """
    try:
        track = Track.objects.get(pk=track_id)
        track.delete()
        return 200
    
    except Track.DoesNotExist as e:
        return 404, {'message': 'Track does not exist'}
