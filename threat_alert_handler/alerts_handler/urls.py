from django.urls import path
from .views import AlertView

urlpatterns = [
   path("alerts/", AlertView.as_view(), name="alerts"),
   path("alerts/<int:pk>/", AlertView.as_view(), name="alert-detail"), 
]
