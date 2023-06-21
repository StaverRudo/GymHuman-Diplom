
from django.contrib import admin
from django.urls import path, include
from users.views import *
from articles.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('signup/', training_signup, name='training_signup'),
    path('confirmation/', training_confirmation, name='training_confirmation'),
]

