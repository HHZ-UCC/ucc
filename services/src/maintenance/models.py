import uuid
from django.db import models

from base.models import Employee
from base.models import Device


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField('date published')
    fk_device = models.ForeignKey(Device, on_delete=models.CASCADE)
    fk_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    
class Hello(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=500)
    fk_employee = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True)
    