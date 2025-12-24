from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import SecurityEvent
from .serializers import SecurityEventSerializer
from rest_framework import status
from users.permissions import IsAdmin

class SecurityEventCreateView(CreateAPIView):
    queryset = SecurityEvent.objects.all()
    serializer_class = SecurityEventSerializer
    permission_classes = [IsAuthenticated]
   
    def create(self, request, *args, **kwargs):
        if not IsAdmin().has_permission(request, self):
            return Response(
                {"status":False, "message": "Admin access required"},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"success": True, "data": serializer.data},
            status=201
        )
