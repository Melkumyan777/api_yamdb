from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, mixins, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import get_tokens_for_user, UserRegistrationSerializer
from .serializers import DummySerializer
from reviews.models import User, Title


class UserRegistrationViewSet(
    mixins.CreateModelMixin, viewsets.GenericViewSet
):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class DummyViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = DummySerializer


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
