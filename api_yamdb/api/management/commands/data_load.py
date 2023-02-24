import csv

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from reviews.models import Category, Comment, Genre, Review, Title

User = get_user_model()


class Command(BaseCommand):
    help = 'load data from csv files'

    def handle(self, *args, **options):
        with open(
            'static\\data\\users.csv', 'r', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                username = row['username']
                email = row['email']
                role = row['role']
                bio = row['bio']
                first_name = row['first_name']
                last_name = row['last_name']
                users = User(
                    id=id,
                    username=username,
                    email=email,
                    role=role,
                    bio=bio,
                    first_name=first_name,
                    last_name=last_name,
                )
                users.save()

        with open(
            'static\\data\\category.csv', 'r', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row4 in csv_reader:
                id = row4['id']
                name = row4['name']
                slug = row4['slug']
                categories = Category(
                    id=id,
                    name=name,
                    slug=slug,
                )
                categories.save()

        with open(
            'static\\data\\genre.csv', 'r', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row5 in csv_reader:
                id = row5['id']
                name = row5['name']
                slug = row5['slug']
                genres = Genre(
                    id=id,
                    name=name,
                    slug=slug,
                )
                genres.save()

        with open(
            'static\\data\\titles.csv', 'r', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row3 in csv_reader:
                id = row3['id']
                name = row3['name']
                year = row3['year']
                category = Category.objects.get(id=row3['category'])
                titles = Title(
                    id=id,
                    name=name,
                    year=year,
                    category=category,
                )
                titles.save()

        with open(
            'static\\data\\genre_title.csv', 'r', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row6 in csv_reader:
                id = row6['id']
                title_id = row6['title_id']
                genre_id = row6['genre_id']
                genre_titles = Title(
                    id=id,
                    title_id=title_id,
                    genre_id=genre_id,
                )
                genre_titles.save()

        with open(
            'static\\data\\review.csv', 'r', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row1 in csv_reader:
                id = row1['id']
                title_id = row1['title_id']
                text = row1['text']
                author = User.objects.get(id=row1['author'])
                score = row1['score']
                pub_date = row1['pub_date']
                reviews = Review(
                    id=id,
                    title_id=title_id,
                    text=text,
                    author=author,
                    score=score,
                    pub_date=pub_date,
                )
                reviews.save()

        with open(
            'static\\data\\comments.csv', 'r', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row2 in csv_reader:
                id = row2['id']
                review_id = row2['review_id']
                text = row2['text']
                author = User.objects.get(id=row2['author'])
                pub_date = row2['pub_date']
                comments = Comment(
                    id=id,
                    review_id=review_id,
                    text=text,
                    author=author,
                    pub_date=pub_date,
                )
                comments.save()
