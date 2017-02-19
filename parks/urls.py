from django.conf.urls import *
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<park_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<park_id>[0-9]+)/favorite$', views.add_favorite_park, name='favorite'),
    url(r'^(?P<park_id>[0-9]+)/unfavorite$', views.unfavorite_park, name='unfavorite'),
    url(r'^[0-9]+/put_rating/$', views.put_rating),
    url(r'^put_rating/$', views.put_rating),
    url(r'^(?P<park_id>[0-9]+)/problem$', views.submit_problem, name='problem'),
    url(r'^problem_submit/$', TemplateView.as_view(template_name='parks/problem_done.html'), name='problem_done'),
]
