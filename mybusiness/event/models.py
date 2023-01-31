from django.db import models
from django_softdelete.models import SoftDeleteModel
from room.models import Room

# Specifying event type choices
TYPE_CHOICES = (
    (1, 'Public'),
    (2, 'Private')
)


class Event(SoftDeleteModel, models.Model):
    """
    Model control for business rooms
    """
    name = models.CharField(max_length=150)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=1)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'event'


class CustomerBook(models.Model):
    """

    """
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    event = models.ForeignKey('event.Event', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'customer_book'
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'last_name', 'event'],
                name='unique_event_per_user')
        ]
