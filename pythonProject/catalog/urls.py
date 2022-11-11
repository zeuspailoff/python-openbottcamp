from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='main-view'),
    path('catalog/templates/movies.html', views.movies, name='main-view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
