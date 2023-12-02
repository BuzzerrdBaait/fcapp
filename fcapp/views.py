from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.views import View 
from .models import *
from django.http import HttpResponse

from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import *
from collections import OrderedDict
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


from django.urls import reverse


User = get_user_model()



def home(request):

    """_____I imported OrderedDict and created an instance of a dictionary of the Deck.Category choices
    _____It sorts by the id # so I had to call lambda function and key[1] is used because the keywords 
    _____are in that column. So basically this is how to sort your items by the category choices defined
    _____in the model's category dictionary.

    """


    return render(request, 'home.html')
