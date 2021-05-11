from django.urls.conf import path
from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
]