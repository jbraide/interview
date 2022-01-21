# rest_framework's APIView
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

# import response
from rest_framework.response import Response

# import model
from .models import URLShortner

# import serializer
from .serializers import CreateShortURLSerializer

# utils
from django.utils.timezone import now
from .utils import create_shortened_url

class CreateShortURLView(GenericAPIView):
    serializer_class = CreateShortURLSerializer

    def get(self, request):
        serializer = self.serializer_class()
        return Response(data = {
            'info':serializer.data,
            })

    def post(self, request, **kwargs):
        # context
        context = kwargs

        # short_url
        shortened_url = create_shortened_url(URLShortner)


        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # get long link 
            long_url = serializer.data['original_url']

            # create instance
            URLShortner(
                created_date_time=now(),
                original_url=long_url,
                short_url=shortened_url
            ).save()

            # actual link
            working_short_url = request.build_absolute_uri('/') + shortened_url

            # tier's link
            tier_mobility_link = 'https://tier.app/'+shortened_url            


            # context
            context['long_link'] = long_url
            context['short_url'] = working_short_url
            context['tier_demo_link'] = tier_mobility_link

            return Response(context)
        else:
            return Response(serializer.errors)

