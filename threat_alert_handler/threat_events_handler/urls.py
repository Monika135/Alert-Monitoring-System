from django.urls import path
from .views import SecurityEventCreateView


urlpatterns = [
    path("security_events/", SecurityEventCreateView.as_view(), name="security_events"),
]
