from django.db import models

# Create your models here.
import secrets

import string

from django.contrib.auth.models import AbstractUser, Group, Permission

from django.db import models




                




class User_Profile(AbstractUser):
    
    email= models.CharField(max_length=40,blank=True,null=True, unique=True)

    authentication_key = models.CharField(max_length=50, unique=True)

    is_verified = models.CharField(max_length=1, default='N')

    user_image = models.ImageField(upload_to='user_images/', blank=True, null=True)

    user_library = models.CharField(max_length=255, default='', blank=True)



    """
    AUTHENTICATION LINK CODE
    """
    authentication_link = models.CharField(max_length=50, default='authenticate_your_acct')

    def generate_unique_link(self):

        link = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(30))

        link = link.replace('\\', str(secrets.randbelow(1000)))

        link = link.replace('/', str(secrets.randbelow(1000)))

        link = link.replace("'", str(secrets.randbelow(1000)))

        link = link.replace('"', str(secrets.randbelow(1000)))

        return link



    def save(self, *args, **kwargs):

        if not self.authentication_key:

            self.authentication_key = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(30))


        if not self.authentication_link:

            self.authentication_link = self.generate_unique_link()


        super().save(*args, **kwargs)
