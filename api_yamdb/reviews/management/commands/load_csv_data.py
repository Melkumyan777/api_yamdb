from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Review, Comment, User


class User(BaseCommand):
    help = 'Загрузка данных из user.csv'

    def handle(self, *args, **options):
        reader = DictReader(open('./static/data/user.csv)'))
        for row in reader:
            user = User(id=row['id'], username=row['username'],
                        email=row['email'], role=['role'], bio=row['bio'],
                        first_name=row['first_name'],
                        last_name=row['last_name'])
            user.save()


class Review(BaseCommand):
    help = 'Загрузка данных из review.csv'

    def handle(self, *args, **options):
        reader = DictReader(open('./static/data/review.csv)'))
        for row in reader:
            review = Review(id=row['id'], title_id=row['title_id'],
                            text=row['text'], author=row['author'],
                            score=row['score'], pub_date=row['pub_date'])
            review.save()


class Comment(BaseCommand):
    help = 'Загрузка данных из comments.csv'

    def handle(self, *args, **options):
        reader = DictReader(open('./static/data/comments.csv)'))
        for row in reader:
            comment = Comment(id=row['id'], review_id=row['review_id'],
                              text=row['text'], author=row['author'],
                              pub_date=row['pub_date'])
            comment.save()
