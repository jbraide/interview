from django.db import models

class URLShortner(models.Model):
    '''
        Url shortner models Definition
        * created_date_time: when the shortened url was created
        * times_followed: to get the number of times the url was followed
        * original_url: the inputed link by the user (i.e the original link)
        * short_url: the shortened url
    '''
    created_date_time = models.DateTimeField()
    times_followed = models.PositiveInteger(default=0)
    original_url = models.URLFIELD()
    short_url = models.CharField(max_length=15, unique=True, blank=True)


    class Meta:
        ordering = ['-created']


    def __str__(self):
        return f'shortened {self.original_url} to {self.short_url}'