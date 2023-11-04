from django.db import models
from management.models import Shortlist, Process, Duty
from users.models import User
from django.utils import timezone

class TimestampedField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)
        if add:
            # Set the value to the current time when creating the row
            value = timezone.now()
        return value

class Round(models.Model):
    #enumeration
    STATUS_CHOICES = [
        ('CLR', 'Cleared'),
        ('AWR', 'Awaiting Result'),
        ('NC', 'Not Cleared'),
        ('NS', 'Not Started'),
        ('O', 'Ongoing'),
    ]

    #field
    round_id = models.AutoField(primary_key=True)
    shortlist_id = models.ForeignKey(Shortlist, on_delete=models.CASCADE, null=False)
    round_number = models.IntegerField(null=False, blank=False)
    round_start = models.DateTimeField(null=True, blank=True)
    round_end = models.DateTimeField(null=True, blank=True)
    room_no = models.CharField(max_length=100, null=True, blank=False, default="")

    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default='NS',
        blank=True,  # Allow the field to be blank
        null=False,  # Do not allow null values
    )

class Location(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)    
    updated_by = models.CharField(max_length=100, null=False, blank=False)  #not needed and display in student profile itself. add error handling  
