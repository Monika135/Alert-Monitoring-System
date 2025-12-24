from rest_framework import serializers
from .models import Alert
from threat_events_handler.serializers import SecurityEventSerializer


class AlertSerializer(serializers.ModelSerializer):

    event = SecurityEventSerializer(read_only=True)

    class Meta:
        model = Alert
        fields = "__all__"