# import django settings
from django.conf import settings

# import choice from random module
from random import choice

from string import ascii_letters, digits


# define the size of the alphanumeric char 
size_of_code = getattr(settings, 'MAXIMUM_URL_CHARS', 13)

# characters and digits
available_characters = ascii_letters + digits

def generate_random_alphanum(chars=available_characters):
    '''
        generate random alphanumberic string based on the 
        range of *size_of_code
    '''
    return ''.join(
        [choice(chars) for _ in range(size_of_code)]
    )

'''
    This function check for the existence of a shorturl 
    if the shorturl does exist 

'''
def create_shortened_url(model_instance):
    random_code = create_random_code()
    # Gets the model class

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        # Run the function again
        return create_shortened_url(model_instance)

    return random_code