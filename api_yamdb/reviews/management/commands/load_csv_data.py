from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Review, Comment, User
from reviews.models import Category, Genre, Title, GenreTitle

PATH = "static/data/"


class Command(BaseCommand):
    help = 'Загрузка данных из static/data'

    def handle(self, *args, **options):
        reader = DictReader(open(f'{PATH}/users.csv', encoding='utf-8'))
        User.objects.all().delete()
        for row in reader:
            user = User(id=row['id'], username=row['username'],
                        email=row['email'], role=['role'], bio=row['bio'],
                        first_name=row['first_name'],
                        last_name=row['last_name'])
            user.save()

        reader = DictReader(open(f'{PATH}/category.csv', encoding='utf-8'))
        Category.objects.all().delete()
        for row in reader:
            category = Category(id=row['id'], name=row['name'],
                                slug=row['slug'])
            category.save()

        reader = DictReader(open(f'{PATH}/genre.csv', encoding='utf-8'))
        Genre.objects.all().delete()
        for row in reader:
            genre = Genre(id=row['id'], name=row['name'], slug=row['slug'])
            genre.save()

        reader = DictReader(open(f'{PATH}/titles.csv', encoding='utf-8'))
        for row in reader:
            title = Title(id=row['id'], name=row['name'], year=row['year'],
                          category_id=row['category'])
            title.save()

        reader = DictReader(open(f'{PATH}/review.csv', encoding='utf-8'))
        for row in reader:
            review = Review(id=row['id'], title_id=row['title_id'],
                            text=row['text'], author_id=row['author'],
                            score=row['score'], pub_date=row['pub_date'])
            review.save()

        reader = DictReader(open(f'{PATH}/comments.csv', encoding='utf-8'))
        for row in reader:
            comment = Comment(id=row['id'], review_id=row['review_id'],
                              text=row['text'], author_id=row['author'],
                              pub_date=row['pub_date'])
            comment.save()

        reader = DictReader(open(f'{PATH}/genre_title.csv', encoding='utf-8'))
        for row in reader:
            genre_title = GenreTitle(id=row['id'], title_id=row['title_id'],
                                     genre_id=row['genre_id'])
            genre_title.save()
