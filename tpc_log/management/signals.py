from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Process, Duty

@receiver(post_save, sender=Process)
def create_row_in_another_table(sender, instance, created, **kwargs):
    if created:
        Duty.objects.create(process_id=instance.process_id, tpc_id=instance.spoc_id)
