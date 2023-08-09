# Third Party Stuff
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

from .common import urlpatterns as base_urlpatterns

urlpatterns = [
    *base_urlpatterns,
    path("v1/users/", include("apps.users.api.v1.urls")),
    # OpenApi configuration
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Redoc UI:
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
