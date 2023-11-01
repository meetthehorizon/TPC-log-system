from django.db import models
from management.models import Shortlist
from users.models import User

class priority(models.Model):
    priority_id = models.AutoField(primary_key=True)
    shortlist_id = models.ForeignKey(Shortlist, on_delete=models.CASCADE, null=False)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    priority = models.IntegerField(null=False, blank=False)
    