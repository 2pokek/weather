from dataclasses import fields
from .models import City
from django.forms import ModelForm, widgets, TextInput, Textarea

class CityForm(ModelForm):
    class Meta:
        model = City
        fields=['name']
        widgets = {'name':TextInput(attrs={"type":"text",
                                           "class":"form-control",
                                           "name":"city",
                                           "placeholder":"Enter your city",
                                           "id":"city"})}