from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'videoteca.views.home', name='home'),
    url(r'^list/$', 'videoteca.views.list_movies', name='list_movies'),
    url(r'^consult/(?P<movie_id>\d+)$', 'videoteca.views.consult_movie', name='consult_movie'),
    url(r'^create/$', 'videoteca.views.create_movie', name='create_movie'),
    url(r'^edit/(?P<movie_id>\d+)$', 'videoteca.views.edit_movie', name='edit_movie'),
    url(r'^delete/(?P<movie_id>\d+)$', 'videoteca.views.delete_movie', name='delete_movie'),
    url(r'^import/(?P<movie_id>\d+)$', 'videoteca.views.import_movie_details', name='import_movie'),
    url(r'^import_all$', 'videoteca.views.import_all_movies', name='import_all_movies')
)
