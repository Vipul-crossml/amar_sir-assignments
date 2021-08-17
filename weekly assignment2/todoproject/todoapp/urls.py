from django.urls import path
from . import views
"""
For updating and deleting the data primary key of the task is used.
"""
urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
]
