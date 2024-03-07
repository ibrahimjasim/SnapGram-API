from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from saved.models import Saved  
from saved.serializers import SavedSerializer


class SavedList(generics.ListCreateAPIView):
    """
    List saved items or create a saved item if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SavedSerializer 
    queryset = Saved.objects.all()  

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)