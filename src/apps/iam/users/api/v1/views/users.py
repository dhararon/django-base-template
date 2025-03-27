# Third Party Stuff
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics

from apps.users.api.v1.serializers import UserDetailSerializer, UserSerializer

# Django Base Template
from apps.users.models import UserModel


@extend_schema_view(
    api_version="1.0",
    get=extend_schema(
        tags=["Users"],
        operation_id="Get user detail",
        description="List all transactions linked to a property.",
        responses={200: UserDetailSerializer},
    ),
)
class UserDetailView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserDetailSerializer


@extend_schema_view(
    api_version="1.0",
    post=extend_schema(tags=["Users"], operation_id="Create user", responses={201: UserSerializer}),
)
class UserCreateView(generics.CreateAPIView):

    queryset = UserModel.objects.none()
    serializer_class = UserSerializer
    # What kind of authentication we'll use?
