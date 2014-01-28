from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'spazaschool.views.landing', name='landing'),
)
