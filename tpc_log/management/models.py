from django.db import models
from users.models import User

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, null=False, blank=False)

class Process(models.Model):
    process_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE, null=False)
    spoc_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role__ne': 'STUDENT'}  # Limit choices to users with role not equal to 'STUDENT'
    )
    venue = models.CharField(max_length=100, null=True, blank=False, default="")
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    hiring_role = models.CharField(max_length=100, null=False, blank=False)

class Duty(models.Model):
    duty_id = models.AutoField(primary_key=True)
    process_id = models.ForeignKey('Process', on_delete=models.CASCADE, null=False)
    tpc_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role__ne': 'STUDENT'}  # Limit choices to users with role not equal to 'STUDENT'
    )

class Shortlist(models.Model):
    shortlist_id = models.AutoField(primary_key=True)
    process_id = models.ForeignKey('Process', on_delete=models.CASCADE, null=False)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

