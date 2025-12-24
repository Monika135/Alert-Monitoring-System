from django.db import models
from threat_events_handler.models import SecurityEvent

class Alert(models.Model):
    STATUS_CHOICES = [
        ("Open", "Open"),
        ("Acknowledged", "Acknowledged"),
        ("Resolved", "Resolved"),
    ]

    event = models.OneToOneField(
        SecurityEvent, on_delete=models.CASCADE, related_name="alert"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Open")
    timestamp = models.DateTimeField(auto_now_add=True)
