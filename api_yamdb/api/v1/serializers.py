from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from reviews.models import User


# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'username')


class UserRegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    username = serializers.SlugField()

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        return user

    class Meta:
        model = User
        fields = ('email', 'username')


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
