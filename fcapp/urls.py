from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

from django.urls import path

from .views import *





app_name = "flashcardgameapp"

urlpatterns = [
     
    path('', views.home, name='home'),

    path('create_deck/', views.create_deck, name='create_deck'),

    path('view_deck/<int:deck_id>/', views.view_deck, name='view_deck'),

    path('add_notes/<int:deck_id>/', add_notes, name='add_notes'),

    path('deck/<int:deck_id>/edit/', views.edit_deck, name='edit_deck'),

    path('create_card/<int:deck_id>/', views.create_card, name='create_card'),

    path('edit_card/<int:card_id>/', views.edit_card, name='edit_card'),

    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),

    path('profile/<int:user_pk>/', views.user_profile_view, name='user_profile'),

    path('about', views.about_us, name='about_us'),

    path('contact', views.contact_view, name='contact'),

    path('clep', views.clep_resources, name='clep'),

    path('login/', views.login_user, name='login'),

    path('resume/', views.resume_page, name='resume'),

    path('webinfo/', views.web_build_info, name='webinfo'),

    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),

    path('register/', views.register, name='register'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('authenticate/<str:authentication_link>/', views.authenticate_user, name='authenticate_user'),
]



