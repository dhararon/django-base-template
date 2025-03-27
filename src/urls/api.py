# Third Party Stuff
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

from urls.common import urlpatterns as base_urlpatterns

urlpatterns = [
    *base_urlpatterns,
    # OpenApi configuration
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Redoc UI:
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
