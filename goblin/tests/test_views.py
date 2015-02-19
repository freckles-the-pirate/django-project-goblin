if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__)))) 

from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from unittest import skip

from goblin.models import *

import logging
logger = logging.getLogger('goblin')

class TestViews(TestCase):
    def setUp(self):
        setup_test_environment()

        # Set up the models we'll use to get the views.
        self.project = Project.objects.create(
            name="Some Django Project",
            slug="some-django-project",
            description="You don't know Django!",
        )
        self.release = Release.objects.create(
            project=self.project,
            version=Version(1, 0),
        )
        self.change = Change.objects.create(
            release=self.release,
            action='+',
            what="Added something!"
        )

        # Set up the client
        self.client = Client()

    def _test_model_view(self, model_inst):
        url = model_inst.get_absolute_url()
        logger.debug("Getting project URL %s"%url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        logger.info(response.content)

    def test_project(self):
        self._test_model_view(self.project)

    def test_release(self):
        self._test_model_view(self.project)
    
    @skip("``Change`` model does not have a " +
          "``get_absolute_url`` method.")
    def test_change(self):
        self._test_model_view(self.change)
