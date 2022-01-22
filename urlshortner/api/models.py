from django.db import models

# import utils
from .utils import create_shortened_url

class URLShortner(models.Model):
    '''
        Url shortner models Definition
        * created_date_time: when the shortened url was created
        * times_followed: to get the number of times the url was followed
        * original_url: the inputed link by the user (i.e the original link)
        * short_url: the shortened url
    '''
    created_date_time = models.DateTimeField()
    times_followed = models.PositiveIntegerField(default=0)
    original_url = models.URLField(max_length=5000)
    short_url = models.CharField(max_length=15, unique=True, blank=True)



    class Meta:
        ordering = ['-created_date_time']


    def __str__(self):
        return f'shortened {self.original_url} to {self.short_url}'

    