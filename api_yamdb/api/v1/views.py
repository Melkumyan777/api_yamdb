from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, mixins, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from django.db.models import Avg

from .serializers import get_tokens_for_user, UserRegistrationSerializer
from .serializers import DummySerializer
from reviews.models import User, Title, Category, Review, Genre
from .filtres import TitleFilter
from .mixins import ModelMixinSet
from .permissions import (AdminModeratorAuthorPermission, AdminOnly,
                          IsAdminUserOrReadOnly)
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer,
                          ReviewSerializer,
                          TitleReadSerializer,
                          TitleWriteSerializer)

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


class CategoryViewSet(ModelMixinSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name', )
    lookup_field = 'slug'


class GenreViewSet(ModelMixinSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name', )
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).all()
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AdminModeratorAuthorPermission,)

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [AdminModeratorAuthorPermission]

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)