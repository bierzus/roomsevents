from django.db import models
from django_softdelete.models import SoftDeleteModel


class Room(SoftDeleteModel, models.Model):
    """
    Model control for business rooms
    """
    number = models.CharField(max_length=5)
    capacity = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'room'

