"""
Sumatra Server

:copyright: Copyright 2010-2015 Andrew Davison
:license: BSD 2-clause, see COPYING for details.
"""

from django.db import models
from django.contrib.auth.models import User
from sumatra.recordstore.django_store.models import Project


class ProjectPermission(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return u"Permission: %s can access %s" % (self.user, self.project)
