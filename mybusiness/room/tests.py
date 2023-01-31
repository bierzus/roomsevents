from django.test import TestCase
from .models import Room
from event.models import Event
from datetime import datetime
from django.utils.timezone import utc


class NewRoomTestCase(TestCase):
    """
    Simple room test
    """

    def setUp(self):
        Room.objects.create(number='1A', capacity=1)

    def test_room_failed_created(self):
        room = Room.objects.filter(number='1A')
        self.assertTrue(room.exists())


class DeleteRoomWithTestCase(TestCase):
    """
    More room test: delete with events
    """
    def setUp(self):
        room = Room.objects.create(number='1A', capacity=2)
        Event.objects.create(name='Event one', type=1, description=None, date=datetime.utcnow().replace(tzinfo=utc), room=room)

    def test_delete_room_with_events(self):
        room = Room.objects.filter(number='1A')
        self.assertFalse(room.delete())


class DeleteRoomWithoutTestCase(TestCase):
    """
    More room test: delete without events
    """
    def setUp(self):
        Room.objects.create(number='1A', capacity=2)

    def test_delete_room_without_events(self):
        room = Room.objects.filter(number='1A')
        room.delete()
        self.assertFalse(Room.objects.filter(number='1A'))

