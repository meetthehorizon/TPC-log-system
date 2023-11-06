from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Round

@receiver(pre_save, sender=Round)
def update_round_info(sender, instance, **kwargs):
    if instance.round1_time_in is not None:
        round_model = instance.round  # Replace 'round' with the actual reference name
        # Update the round_number to 1
        round_model.round_number = 1

        # Update round1intime
        round_model.round_start = instance.round1_time_in
        round_model.save()
