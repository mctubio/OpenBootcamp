from django.urls import re_path as url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^films/$', views.FilmListView.as_view(), name='films'),
    url(r'^fimls/(?P<pk>\d+)$', views.FilmDetailView.as_view(), name='film-detail'),
    url(r'^director/$', views.DirectorListView.as_view(), name='director'),
    url(r'^director/(?P<pk>\d+)$', views.DirectorDetailView.as_view(), name='director-detail'),
]
