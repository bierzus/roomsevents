from .models import Room
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from event.serializers import EventSerializer


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    """

    """
    number = serializers.CharField(
        required=True,
        max_length=5,
        validators=[UniqueValidator(queryset=Room.objects.all())]
    )
    capacity = serializers.IntegerField(required=True, min_value=1)
    events = EventSerializer(many=True, required=False)

    class Meta:
        model = Room
        fields = ['number', 'capacity', 'events']
