from django.forms import ModelForm, ModelChoiceField, CharField, TextInput, Textarea, Select
from .models import Author, Tag, Quote


class AuthorForm(ModelForm):
    fullname = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    born_date = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    born_location = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(widget=Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Author
        fields = ('fullname', 'born_date', 'born_location', 'description')


class QuoteForm(ModelForm):
    quote = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    author = ModelChoiceField(queryset = Author.objects.all(), widget=Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Quote
        fields = ('quote', 'author')


class TagForm(ModelForm):
    name = CharField(max_length=50, widget=TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Tag
        fields = ('name',)