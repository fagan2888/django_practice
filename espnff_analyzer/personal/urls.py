from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rankings', views.rankings, name='rankings'),
    url(r'^rankings/([0-9]{8})/([0-9]{2})/$', views.rankings, name="rankings")
]