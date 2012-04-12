from django.db import models
from django import forms
from data.models import Item, User, Filter

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'category', 'price', 'image')

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('cell_phone', 'location')

class FilterForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = ('search_query', 'max_price')
