# Third Party Stuff
from django.conf import settings
from django.urls import include, path

urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        path("watchman/", include("watchman.urls")),
        path("__debug__/", include("debug_toolbar.urls")),
    ]
