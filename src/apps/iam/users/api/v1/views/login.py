# Third Party Stuff
from django.contrib.auth import login
from drf_spectacular.utils import extend_schema, extend_schema_view
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer


@extend_schema_view(
    api_version="1.0",
    post=extend_schema(
        tags=["Login"],
        operation_id="Login user",
        description="Create user token.",
        responses={201: {"token": "uuid"}},  # Change for schema
    ),
)
class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super().post(request)
