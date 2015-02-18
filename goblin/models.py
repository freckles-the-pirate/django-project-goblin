if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.abspath(__file__)))

from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

import re, math, logging
logger = logging.getLogger('goblin')

class Version(list):

    RELEASE=0
    TEST=-1
    BETA=-2
    ALPHA=-3
    DEV=-4

    _STAGES = (RELEASE, TEST, ALPHA, BETA, DEV)

    def __init__(self, *args):
        self.stage = Version.RELEASE
        if args[-1] in Version._STAGES:
            self.stage = args[-1]
            args = args[:-1] # simulating pop()
        for i in range(0, len(args)):
            if not isinstance(args[i], int):
                raise ValueError("Expected type of element %d to be"%i +
                                 " int. Got %s instead."%type(args[i]))
        super(Version, self).__init__(args)

    def _lst_convert(self, ver):
        l1 = list(ver)
        l1.append(ver)
        
    def _are_eq(l1, l2):
        return (l1 == l2) and self._are_eq(l1[1:], l2[1:])

    def __eq__(self, other):
        logger.debug("%s EQUALS %s"%(self, other))
        eq = super(Version, self).__eq__(other) 
        logger.debug("eq? %s, self(%s) == other(%s)?"%(eq, self.stage,
                                                       other.stage))
        return (eq and self.stage == other.stage)

    def __gt__(self, other):
        logger.debug("self(%s) GREATER THAN other(%s)"%(self, other))
        gt = super(Version,self).__gt__(other)
        eq = super(Version, self).__eq__(other)
        c = other.stage > self.stage
        logger.debug("gt? %s, eq? %s; other(%d)"%(gt, eq, other.stage) +
                     " > self(%d) ? %s"%(self.stage, c))
        return ((eq and c) or gt)

    def __lt__(self, other):
        logger.debug("self(%s) LESS THAN other(%s)"%(self, other))
        lt = super(Version,self).__lt__(other)
        eq = super(Version, self).__eq__(other)
        c = self.stage < other.stage
        logger.debug("lt? %s, eq? %s; other(%d)"%(lt, eq, other.stage) +
                     " < self(%d) ? %s"%(self.stage, c))
        return ((eq and c) or lt)

    def __str__(self):
        return unicode(self)

    def __unicode__(self):
        s = '.'.join([str(i) for i in self])
        if self.stage == Version.ALPHA:
            s = s + 'a'
        elif self.stage == Version.BETA:
            s = s + 'b'
        elif self.stage == Version.TEST:
            s = s + '-test'
        elif self.stage == Version.DEV:
            s = s + '-dev'
        return s

    @classmethod
    def from_str(Klass, string):
        return Klass(*[int(i) for i in string.split('.')])

    def to_db(self):
        return '.'.join([str(i) for i in self]) + '.' + str(self.stage)

class VersionField(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs.update({'max_length' : 30})
        super(VersionField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char(500)'

    def to_python(self, value):
        if isinstance(value, Version):
            return value
        elif isinstance(value, str) or isinstance(value, unicode):
            return Version.from_str(value)
        logger.warn("%s could not be converted to %s"%(type(value),
                                                       type(self)))
        return None

    def get_prep_value(self, value):
        return value.to_db()

class Project(models.Model):
    name = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400,
        help_text=_("Short name for the project"))
    description = models.TextField()
    logo = models.ImageField()
    README = models.TextField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    
    def get_absolute_url(self):
        kwargs = {
            'slug' : self.slug,
        }
        return reverse('goblin.views.show_project', kwargs=kwargs)

    class Meta:
        verbose_name="Project"
        verbose_name_plural="Projects"

class NotLatestVersionException(ValidationError):

    def __init__(self, given, expected):
        """ Raised if a given version was expected to be greater than or
        equal to another version.

        :param given: Given version that was flagged.
        :type given: Version

        :param expected: Version that was expected to be the latest.
        """
        self.given = given
        self.expected = expected

    def __str__(self):
        return str("Expected a version higher than %s. "%self.expected +
            "Recieved %s"%self.given)

    def __repr__(self):
        return str("Expected a version higher than %s. "%self.expected +
            "Recieved %s"%self.given)

class Release(models.Model):
    
    project = models.ForeignKey(Project)
    version = VersionField()
    download = models.URLField(blank=True, null=True)
    release_logo = models.ImageField(blank=True, null=True,
        help_text=_("Leaving blank will use the project's logo."))

    def save(self, *args, **kwargs):
        self.clean()
        return super(Release, self).save(*args, **kwargs)

    def clean(self):
        logger.debug("Cleaning a release.")
        latest = None
        if self.project:
            logger.debug("Finding latest version...")
            for r in self.project.release_set.all():
                """ NOTE that r.version is not a VersionField as expected.
                This is due to the Python error
                https://code.djangoproject.com/ticket/14518
                """
                latest = Version.from_str(r.version)
            logger.debug("Latest version is %s."%latest)
            if latest and (self.version < latest):
                raise NotLatestVersionException(self.version, latest)
                
    def get_absolute_url(self):
        kwargs = {
            'project_slug' : self.project.slug,
            'version' : str(self.version),
        }
        return reverse('griffin.views.project_release', kwargs=kwargs)

    class Meta:
        verbose_name='Release'
        verbose_name_plural='Releases'

class Change(models.Model):
    ACTIONS = (
        ('+', "Add"),
        ('-', "Remove"),
        ('*', "Fix"),
        ('>', "Other"),
    )
    release = models.ForeignKey(Release)
    action = models.CharField(choices=ACTIONS, max_length=3)
    what = models.TextField()

    class Meta:
        verbose_name='Change'
        verbose_name_plural='Changes'
        app_label='goblin'

