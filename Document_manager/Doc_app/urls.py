from django.urls import path
from . import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('log',views.log,name='log'),
    path('save',views.save,name='save'),
    path('login/',views.login,name='login'),
    path('list_doc/',views.list_doc,name='list_doc'),
    # path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('report/', views.report, name="report"),
]