from datetime import datetime
from .models import Event, CustomerBook
from rest_framework import serializers
from .models import TYPE_CHOICES
import pytz
from room.models import Room
from django.core import validators


class EventSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    name = serializers.CharField(required=True)
    type = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length=255, required=False, allow_null=True)
    date = serializers.DateTimeField(required=True)
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all().values_list('id', flat=True), required=True)

    def validate(self, data):
        """
        Validate event type, date and room
        """
        # Check event type:
        if not any(int(data['type']) in item for item in TYPE_CHOICES):
            raise serializers.ValidationError(
                {"type": "Event type out of range. 1 for public events and 2 for private"})

        # Check event date
        if data['date'] < datetime.now().replace(tzinfo=pytz.utc):
            raise serializers.ValidationError({"date": "Event date not valid"})

        # Check that there are no events for this day
        room_day_events = Event.objects.filter(
            date__year=data['date'].year,
            date__month=data['date'].month,
            date__day=data['date'].day)
        if room_day_events:
            raise serializers.ValidationError({"date": "This day already has an event"})

        # Check if room exists
        try:
            Room.objects.get(pk=data['room'])
            # Need object not integer!
            data['room'] = Room.objects.get(pk=data['room'])
        except Room.DoesNotExist:
            raise serializers.ValidationError({"room": "This room does not exist"})

        return data

    class Meta:
        model = Event
        fields = ['name', 'type', 'description', 'date', 'room']


class CustomerBookSerializer(serializers.HyperlinkedModelSerializer):
    """

    """
    first_name = serializers.CharField(required=True, max_length=200)
    last_name = serializers.CharField(required=True, max_length=200)
    email = serializers.EmailField(
        required=True,
        validators=[validators.EmailValidator(message='Invalid email format')]
    )
    event = serializers.IntegerField(required=True)

    def validate(self, data):
        # Check if event exists
        try:
            event = Event.objects.get(pk=data['event'])
            # Need object not integer!
            data['event'] = Event.objects.get(pk=data['event'])
        except Event.DoesNotExist:
            raise serializers.ValidationError({"event": "This event does not exist"})
        else:
            # Check event type (only public)
            if event.type != 1:
                raise serializers.ValidationError({"event": "You can only book public events"})
            # Check availability
            all_books = CustomerBook.objects.filter(event=data['event']).count()
            room = Room.objects.get(pk=event.room.id)
            if all_books == room.capacity:
                raise serializers.ValidationError({"event": "There are no places in this event"})
            # Check multiple books for this user
            exists = CustomerBook.objects.filter(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                event=data['event']
            )
            if exists:
                raise serializers.ValidationError({"event": "You have already booked for this event"})

        return data

    class Meta:
        model = CustomerBook
        fields = '__all__'

