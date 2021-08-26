from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # 
    
    path('artist', views.artist, name='artist'),
    # 
    
    path('award', views.award, name='award'),
    # 
    
    path('rating', views.rating, name='rating'),
    # 

    path('avg1', views.avg1, name='avg1'),
    # 
]