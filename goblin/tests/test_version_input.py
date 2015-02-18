if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__)))) 

from django.test import TestCase
from goblin.models import Version, VersionField

import logging
logger = logging.getLogger('goblin')

class TestVersionInput(TestCase):

    def setUp(self):
        self.field = VersionField()

    def test_to_python(self):
        expected = Version(1, 3, 4, Version.ALPHA)
        self.assertEqual(self.field.to_python('1.3.4.-1'), expected)

    def test_get_prep_value(self):
        v = Version(1, 3, 4, Version.ALPHA)
        expected = '1.3.4.-3'
        self.assertEqual(self.field.get_prep_value(v), expected)

    def get_db_prep_value(self):
        self.assertEqual(
            self.field.get_db_prep_value(Version(1, 3, 4, Version.ALPHA),
                                         None), '1.3.4.-1')
