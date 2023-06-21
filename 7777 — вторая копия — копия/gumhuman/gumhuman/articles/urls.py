
from django.contrib import admin
from django.urls import path, include
from articles.views import *
from django.conf.urls.static import static
from django.conf import settings
from users.views import article_detail
from . import views
from .views import todo

app_name = 'articles'

urlpatterns = [
    path('', about, name='about'),
    path('articles/search/', views.article_search, name='article_search'),
    #  path('<int:article_id>/', article_detail, name='article_detail'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('page/<int:page>/', about, name='about_page'),
    path('tolist/', todo, name='todo'),
    path('calories/', calories, name='calories'),
    path('video/', video, name='video'),
    path('hand/', hand, name='hand'),
    path('shoulders/', shoulders, name='shoulders'),
    path('back/', back, name='back'),
    path('foot/', foot, name='foot'),
    path('chest/', chest, name='chest'),
    path('prace/', prace, name='prace'),
    path('raspisanie/', raspisanie, name='raspisanie'),
    path('filter/', article_filter, name='article_filter'),
    path('feedback/', feedback, name='feedback'),
    path('inbox/', inbox, name='inbox'),
    path('reply/<int:message_id>/', views.reply, name='reply'),
]

