# app/urls.py

from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dank/$', views.dank, name='dank'),
    url(r'^profile/$', views.profile, name='profile'),
]
