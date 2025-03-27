# Third Party Stuff
from django.contrib import admin
from django.urls import path

from .common import urlpatterns as base_urlpatterns

urlpatterns = [
    *base_urlpatterns,
    path("", admin.site.urls),
]
