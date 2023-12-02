"""
APP URLS.PY
"""

from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

from django.urls import path

from .views import *





app_name = "fcapp"

urlpatterns = [
     
    path('', views.home, name='home'),

]


from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

from django.urls import path

from .views import *





app_name = "flashcardgameapp"

urlpatterns = [
     
    path('', views.home, name='home'),

    path('admin/', admin.site.urls),

]
