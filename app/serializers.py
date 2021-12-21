from .models import Category,RandomList
from rest_framework import serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class RandomListSerializer(serializers.ModelSerializer):
    class Meta:
        model=RandomList
        fields="__all__"