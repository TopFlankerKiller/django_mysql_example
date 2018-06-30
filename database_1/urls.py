from django.shortcuts import render
from django.conf.urls import url
from . import views


# This url list indicates connections between urls and certain functions inside python code which can deliver content as a view.
urlpatterns = [
    url(r'^$', views.get_user_has_occupation, name='get_user_has_occupation')
]


