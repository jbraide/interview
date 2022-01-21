# rest_framework's APIView
from rest_framework.view import APIView
from rest_framework.generics import GenericAPIView

# import response
from rest_framework.response import Response

# import model
from .models import URLShortner

# import serializer
from .serializers import CreateShortURLSerializer

class CreateShortURL(APIView):
    serializer_class = CreateShortURLSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class()
        return Response(serializer.data)

