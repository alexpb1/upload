from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('makeuploadurl', views.makeupload, name='makeupload'),
    path('showupload', views.showupload, name='showupload'),
            ]
