from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Event
from .serializers import EventSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Sets the organizer to the user who makes the request
        serializer.save(organizer=self.request.user)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Optionally restricts the returned events to those with a status
        indicating they are upcoming, if the 'upcoming' query parameter
        is set in the URL.
        """
        queryset = self.queryset
        if 'upcoming' in self.request.query_params:
            queryset = queryset.filter(start_time__gt=timezone.now())
        return queryset