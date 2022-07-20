from this import s

#SLUG IS FOR SCALABILITY IN CODE 

from django.utils.text import slugify

import string
import random



def generate_random_string(N):
    res=''.join(random.choices(string.ascii_uppercase+string.digits,k=N))

    return res 

def generate_slug(text):
    new_slug=slugify(text)
    from src.models import BlogModel
    if BlogModel.objects.filter(slug=new_slug).exists():
        generate_slug(text + generate_random_string(s))
    return new_slug


