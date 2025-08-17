from rest_framework import serializers
from .models import Dog, Owner, Walker, Walk

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class WalkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walker
        fields = '__all__'

class WalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walk
        fields = '__all__'
