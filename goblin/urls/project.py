from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns

urlpatterns = patterns('',
    url(r'^$/', 'goblin.views.project', name='show_project'),
    url(r'^/release/(?P<release>[\d\.]*\d+[\-\w]){1,10}$',
        'goblin.views.show_project',
        name='show_project_release'),
)
