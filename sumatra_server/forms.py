"""
Sumatra Server

:copyright: Copyright 2010-2014 Andrew Davison
:license: CeCILL, see COPYING for details.
"""

from django.forms import ModelForm
from sumatra_server.models import ProjectPermission


class PermissionsForm(ModelForm):

    class Meta:
        model = ProjectPermission
        fields = ('user',)
