from bson.objectid import ObjectId

from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongodb
from .models import Quote, Author, Tag
from .forms import QuoteForm, AuthorForm, TagForm

def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

def author(request, author_id):
    author = Author.objects.get(author_id)
    return render(request, "quotes/author.html", {'form': AuthorForm()})