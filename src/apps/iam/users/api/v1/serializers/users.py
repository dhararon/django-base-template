# Third Party Stuff
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Django Base Template
from apps.users.models import UserModel


class UserSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    status = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=UserModel.objects.all(),
                message="This email is already registered",
            ),
        ],
    )

    class Meta:
        model = UserModel
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "status",
            "is_active",
        )


class UserDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    status = serializers.CharField()
    is_active = serializers.BooleanField()
