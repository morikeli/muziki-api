from ninja import ModelSchema, Schema
from ninja.orm import create_schema
from api.models import Track


class TrackSchema(ModelSchema):
    """ This is a track data schema. It is representation of reponse data after sending a request. """
    class Config:
        model = Track
        model_fields = ['title', 'artist', 'duration', 'last_play']
        # model_exclude = ['id']


# this also works - you can use this or method 1, i.e. `class TrackSchema(ModelSchema)`
# TrackSchema = create_schema(Track, fields=['title', 'artist', 'duration', 'last_play'])

class TrackNotFoundSchema(Schema):
    """ This is a data schema for response data if no track is found. """
    message: str

