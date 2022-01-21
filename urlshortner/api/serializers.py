from rest_framework import serializers

# model
from .models import URLShortner
class LongURLSerializer(serializers.ModelSerializer):
    long_url = serializers.URLField(max_length=300)

    class Meta:
        model = URLShortner
        fields = ['long_url',]
