from rest_framework import viewsets
from .models import Dog, Owner, Walker, Walk
from .serializers import DogSerializer, OwnerSerializer, WalkerSerializer, WalkSerializer

class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class WalkerViewSet(viewsets.ModelViewSet):
    queryset = Walker.objects.all()
    serializer_class = WalkerSerializer

class WalkViewSet(viewsets.ModelViewSet):
    queryset = Walk.objects.all()
    serializer_class = WalkSerializer
