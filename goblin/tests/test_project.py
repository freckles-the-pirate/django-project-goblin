if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__)))) 

from django.test import TestCase
from goblin.models import *

import logging
logger = logging.getLogger('goblin')

class TestProject(TestCase):

    def setUp(self):
        self.project = Project(
            name = 'Silly Song',
            description = 'Sing a silly song.')
        self.releases = (
            Release( version=Version(0, 1, Version.ALPHA)),
            Release( version=Version(1, 2, Version.DEV)),
            Release( version=Version(1, 0)))
        self.changes = (
            (Change(release=self.releases[0], action='+',
                    what="Add silly song."),),
            (Change(release=self.releases[1], action='=',
                    what="Silly song wasn't silly enough. Change it."),
             Change(release=self.releases[1], action='-',
                    what="Laugh track."), ),
        )

    def test_simple_project_creation(self):
        """ A basic project can be created.
        """
        self.project.save()
        for r in range(0, len(self.releases[:-1])):
            self.project.release_set.add(self.releases[r])
            self.releases[r].save()
            for c  in self.changes[r]:
                self.releases[r].change_set.add(c)
                c.save()
            self.project.save()

    def test_throw_incorrect_version(self):
        """ NotLatestVersionException is raised if a release is added with
        a version that is not the latest version.
        """
        self.test_simple_project_creation()
        with self.assertRaises(NotLatestVersionException):
            self.project.release_set.add(self.releases[-1])
            self.releases[-1].save()
        
