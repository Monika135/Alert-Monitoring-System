from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SecurityEvent, Alert

@receiver(post_save, sender=SecurityEvent)
def create_alert(sender, instance, created, **kwargs):
    if created and instance.severity in ["High", "Critical"]:
        Alert.objects.create(event=instance)
