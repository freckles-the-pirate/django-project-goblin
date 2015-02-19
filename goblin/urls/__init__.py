from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns

urlpatterns = patterns('',
    url(r'^$', 'goblin.views.list_projects', name='project_list'),
    url(r'^(?P<project_slug>[\-\w\d]+)/',
        include('goblin.urls.project')
   ),
)
