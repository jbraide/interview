from rest_framework import serializers

# model
from .models import URLShortner


class CreateShortURLSerializer(serializers.Serializer):
    original_url = serializers.URLField(max_length=300)