from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews/', views.reviews, name='reviews'),
    path('add_docfile/', views.add_docfile, name='add_docfile'),
    path('reviews/<str:name>', views.revision, name='revision'),
]
