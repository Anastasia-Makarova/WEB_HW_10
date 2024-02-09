from django.forms import ModelForm, ModelChoiceField, CharField, TextInput, Textarea, Select
from .models import Author, Tag, Quote



class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, required=True, widget=TextInput(attrs={'class': 'form-control', 'id': 'AuthorName'}))
    born_date = CharField(max_length=50, widget=TextInput(attrs={'class': 'form-control', 'id': 'AuthorBornAt'}))
    born_location = CharField(max_length=150, widget=TextInput(attrs={'class': 'form-control', 'id': 'AuthorBornIn'}))
    description = CharField(widget=Textarea(attrs={'class': 'form-control', 'id': 'AuthorDescription'}))


    class Meta:
        model = Author
        fields = ('fullname', 'born_date', 'born_location', 'description')


class QuoteForm(ModelForm):
    quote = CharField(required=True, widget=TextInput(attrs={'class': 'form-control', 'id': 'QuoteText'}))
    author = ModelChoiceField(queryset = Author.objects.all(), widget=Select(attrs={'class': 'form-control', 'id': 'QuoteAuthor'}))

    class Meta:
        model = Quote
        fields = ('quote', 'author')


class TagForm(ModelForm):
    name = CharField(max_length=30, widget=TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Tag
        fields = ('name',)