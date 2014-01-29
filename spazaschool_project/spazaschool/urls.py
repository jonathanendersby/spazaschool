from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'spazaschool.views.landing', name='landing'),
    url(r'^login/$', 'spazaschool.views.login', name='login'),
    url(r'^logout/$', 'spazaschool.views.logout', name='logout'),
    url(r'^register/$', 'spazaschool.views.register', name='register'),
)
