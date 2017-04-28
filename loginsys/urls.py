from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.registration, name='registration'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
