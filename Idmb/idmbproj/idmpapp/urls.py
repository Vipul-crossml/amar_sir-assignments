from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/results/', views.results, name='results'),
    path('<int:movie_id>/response/', views.response, name='response'),
]