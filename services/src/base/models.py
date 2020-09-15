import uuid
from django.db import models


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_id = models.CharField(max_length=250, unique=True)
    lastname = models.CharField(max_length=30)
    surname = models.CharField(max_length=250)

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_id = models.CharField(max_length=250, unique=True)
    type = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    created_at = models.DateTimeField('date published')