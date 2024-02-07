import django
import os

from pymongo import MongoClient


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_project.settings')
django.setup()

from quotes.models import Quote, Tag, Author

client = MongoClient('mongodb://localhost')

db = client.HW10

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []

    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
