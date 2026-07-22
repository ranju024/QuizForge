import uuid

from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    '''
    Abstract Base Model that provides created and update timestamps.
    No database table is created for this class
    '''
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    class Meta:
        abstract = True # tells django not to create a table for this model

        