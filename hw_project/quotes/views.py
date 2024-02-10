from bson.objectid import ObjectId

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


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
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(author)})
    return render(request, "quotes/author.html", context={'author': author})

@login_required
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

def normalize_tags(tags): 
    return tags.split(',')

@login_required
def add_quote(request):
    
    form = QuoteForm(instance=Quote())
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=Quote())
        tags = request.POST['tags']
        if tags == '':
            return render(request, 'quotes/add_quote.html',
                  context={'quote_form': form})
        if form.is_valid():
            db = get_mongodb()
            db.quotes.insert_one({
                'author': form.cleaned_data["quote"],
                'tags': normalize_tags(tags),
                'author': form.cleaned_data["author"],

                })
            # quote = quote_form.save(commit=False)
            # quote.user = request.user
            # quote.save()
            # for t in list_tags:
            #     tag = Tag.objects.get_or_create(name = t)
            #     quote.tags.add(tag[0])
            return redirect(to='/')
    return render(request, 'quotes/add_quote.html', context={'quote_form': form})