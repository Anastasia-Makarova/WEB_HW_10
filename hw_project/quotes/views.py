from bson.objectid import ObjectId

from django.shortcuts import render, redirect
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

def author(request, author):
    author = Author.objects.get(author)
    return render(request, "quotes/author.html", context={'author': author})

def add_author(request):
    form = AuthorForm(instance=Author())
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            db = get_mongodb()
            db.authors.insert_one({
                'fullname': form.cleaned_data["fullname"],
                'born_date': form.cleaned_data["born_date"],
                'born_location': form.cleaned_data["born_location"],
                'description':form.cleaned_data["description"]
                })
            
            return redirect(to='/')

    return render(request, 'quotes/add_author.html', context={'form': form})

def add_quote(request):
    txt = "add quote"
    return render(request, 'quotes/add_quote.html', context={'add_quote': txt})