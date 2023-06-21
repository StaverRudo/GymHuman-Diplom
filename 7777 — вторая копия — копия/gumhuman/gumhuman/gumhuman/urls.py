from django.contrib import admin
from django.urls import path, include
from articles.views import *
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('articles/', include('articles.urls', namespace='articles')),
    path('users/', include('users.urls', namespace='users')),
    # path('about/', about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error_404    
