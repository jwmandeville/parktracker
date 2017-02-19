from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin
from parks import views
from django.contrib.auth import views as built_in_views
from django.views.generic.base import RedirectView
from . import auth_views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='parks', permanent=False), name='home'),
    url(r'^accounts/login/$', RedirectView.as_view(url=reverse_lazy('login'), permanent=False), name='go_to_login'),
    url(r'^parks/', include('parks.urls', namespace="parks")),
    url(r'^admin/', include(admin.site.urls)),
    url('^password-change/', built_in_views.password_change, name='password_change'),
    url('^login/', built_in_views.login, name='login'),
    url(r'^password_reset/$', built_in_views.password_reset, name='password_reset'),
    url(r'^password_reset_done/$', built_in_views.password_reset_done, name='password_reset_done'),
    url(r'^password_reset_complete/$', built_in_views.password_reset_complete, name='password_reset_complete'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', built_in_views.password_reset_confirm, name='password_reset_confirm'),
    url('^logout/', auth_views.logout_view, name='logout'),
    url(r'^create-account/$', auth_views.add_user, name='add_user'),
    url(r'^admin/parse', views.get_data, name='parse'),
    url(r'^admin/clear', views.clear_data, name='clear'),
]
