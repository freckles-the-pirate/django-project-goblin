if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__)))) 

from django.test import TestCase
from goblin.models import Version

import logging
logger = logging.getLogger('goblin')

class TestVersion(TestCase):

    def setUp(self):
        pass

    def test_creation(self):
        version = Version(0, 1, Version.ALPHA)
        self.assertIsNotNone(version)

    def test_exception(self):
        with self.assertRaises(ValueError):
            Version('invalid', 'value')

    def test_string(self):
        v1 = Version(3, 4, 1)
        v2 = Version(0, 1, Version.ALPHA)
        self.assertEqual(str(v1), '3.4.1')
        self.assertEqual(str(v2), '0.1a')

    def test_comparison(self):
        self.assertTrue(Version(3, 4, 2) > Version(3, 2, 1))
        self.assertTrue(Version(10, 9) > Version(1, 3, 4, Version.ALPHA)),
        self.assertTrue(Version(1, 4) == Version(1, 4))
        self.assertTrue(Version(4, 8, Version.BETA) >
                         Version(4, 8, Version.ALPHA))
        self.assertTrue(Version(4, 8, Version.DEV) <
                         Version(4, 8, Version.ALPHA))
