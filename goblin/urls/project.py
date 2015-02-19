from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns

from goblin.models import VERSION_REGEXP

urlpatterns = patterns('',
    url(r'^$', 'goblin.views.show_project', name='show_project'),
    url(r'^/release/(?P<version>%s)$'%VERSION_REGEXP,
        'goblin.views.show_project',
        name='show_project_release'),
)
