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

# exceptions
from django.http import Http404
from rest_framework.exceptions import NotFound

class CreateShortURLView(APIView):
    serializer_class = CreateShortURLSerializer

    def get(self, request):
        serializer = self.serializer_class()
        return Response(data = {
            'welcome_message':'Welcome to the URL shortening API, Kindly send a POST request or fill the form with a valid url (*starts with https:// or http://) to generate a short link',
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
            tier_mobility_url = 'https://tier.app/'+shortened_url            


            # context
            context['long_url'] = long_url
            context['short_url'] = working_short_url
            context['tier_demo_url'] = tier_mobility_url

            return Response(context)
        else:
            return Response(serializer.errors)

class GetLongURLView(APIView):
    
    def get(self, request, short_url):
        # get the short url query
        short_url_query = self.get_object(short_url)        

        # get the long url/original url
        long_url = short_url_query.original_url

        # update the times_followed
        times_followed = short_url_query.times_followed
        times_followed += 1
        URLShortner.objects.update(times_followed=times_followed)

        return Response(data={
            'long_url': long_url, 
            'times_followed': times_followed,
        })

    def get_object(self, short_url):
        
        try:
            return URLShortner.objects.get(short_url=short_url)
        except:
            raise NotFound(detail='Sorry the url you\'re looking for seems broken')