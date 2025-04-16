"""
Sumatra Server

:copyright: Copyright 2010-2020 Andrew Davison
:license: BSD 2-clause, see COPYING for details.
"""

from django.urls import re_path
from sumatra_server.views import (
    RecordResource,
    ProjectResource,
    ProjectListResource,
    PermissionListResource,
)

urlpatterns = [
    re_path(r"^$", ProjectListResource.as_view(), name="sumatra-project-list"),
    re_path(r"^(?P<project>[^/]+)/$", ProjectResource.as_view(), name="sumatra-project"),
    re_path(
        r"^(?P<project>[^/]+)/permissions/$",
        PermissionListResource.as_view(),
        name="sumatra-project-permissions",
    ),
    re_path(
        r"^(?P<project>[^/]+)/(?P<label>\w+[\w|\-\.]*)/$",
        RecordResource.as_view(),
        name="sumatra-record",
    ),
]
