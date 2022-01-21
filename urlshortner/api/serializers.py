from rest_framework import serializers

class LongURLSerializer(serializers.Serializer):
    long_url = serializers.URLField(max_length=300)
