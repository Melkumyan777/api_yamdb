from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, mixins, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .email import send_token
from .serializers import get_tokens_for_user, UserRegistrationSerializer
from reviews.models import User


class UserRegistrationViewSet(
    mixins.CreateModelMixin, viewsets.GenericViewSet
):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.get(username=serializer.validated_data['username'])
        send_token(user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST'])
def get_token(request):
    for arg in ('username', 'confirmation_code'):
        if not request.data.get(arg):
            return Response(
                {arg: ["This field is required."]},
                status=status.HTTP_400_BAD_REQUEST
            )
    user = get_object_or_404(User, username=request.data['username'])
    if request.data['confirmation_code'] == user.get_hash():
        user.email_is_verified = True
        user.save()
        return Response(get_tokens_for_user(user), status=status.HTTP_200_OK)
    return Response(
        f'Confirmation code {request.data["confirmation_code"]} is  incorrect!'
        ' Be sure to request it again',
        status=status.HTTP_400_BAD_REQUEST
    )
