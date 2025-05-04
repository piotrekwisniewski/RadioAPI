from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Hit
from .serializers import HitSerializer

class HitListCreateAPIView(generics.ListCreateAPIView):
    """
    Covers:
    - GET /api/v1/hits (for list of the 20 newest tracks)
    - POST /api/v1/hits (adding new track)
    """
    queryset = Hit.objects.all().order_by('-created_at')[:20]
    serializer_class = HitSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Endpoint name
    def get_view_name(self):
        return "RestHits radio list API"

class HitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Covers:
    - GET /api/v1/hits/{title_url} (track details)
    - PUT /api/v1/hits/{title_url} (track details update)
    - DELETE /api/v1/hits/{title_url} (track removing)
    """
    queryset = Hit.objects.all()
    serializer_class = HitSerializer
    lookup_field = 'title_url'

    # Ensdpoint name
    def get_view_name(self):
        return "Track details API"
