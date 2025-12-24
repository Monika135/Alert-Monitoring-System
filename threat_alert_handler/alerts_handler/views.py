# alerts/views.py
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from .models import Alert
from .serializers import AlertSerializer
from users.permissions import IsAdmin


class AlertView(GenericAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status", "event__severity"]

    def get(self, request):
        alerts = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(alerts, many=True)
        return Response(
            {"status": True, "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def patch(self, request, pk=None):
        if not IsAdmin().has_permission(request, self):
            return Response(
                {"status": False, "message": "Admin access required"},
                status=status.HTTP_403_FORBIDDEN,
            )

        try:
            alert = Alert.objects.get(pk=pk)
        except Alert.DoesNotExist:
            return Response(
                {"status": False, "message": "Alert not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.get_serializer(alert, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"success": True, "data": serializer.data},
            status=status.HTTP_200_OK,
        )
