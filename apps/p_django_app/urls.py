from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^add_friend/(?P<id>\d+)$', views.add_friend),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^view/(?P<id>\d+)$', views.view),
    url(r'^home/(?P<id>\d+)$', views.home),
]
