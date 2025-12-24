from django.db import models

class SecurityEvent(models.Model):
    SEVERITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Critical", "Critical"),
    ]

    EVENT_TYPES = [
        ("intrusion", "Intrusion"),
        ("malware", "Malware"),
        ("anomaly", "Anomaly"),
    ]

    source_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
