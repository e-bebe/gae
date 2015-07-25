from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^hello/yokkora$', 'apps.hello.views.yokkora'),
)
