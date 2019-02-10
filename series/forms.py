from django import forms
from .models import TVShow 
from .validators import validate_name

class SeriesCreateForm(forms.Form):
  name        = forms.CharField()
  summary     = forms.CharField(required=False)
  imdb        = forms.CharField(required=False)

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if name == "":
       raise form.ValidationError("Name must be complete")
    return name

class TVShowCreateForm(forms.ModelForm):
  class Meta:
    model = TVShow
    fields = [
      'name', 
      'summary', 
      'imdb' 
    ]    

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if name == "":
       raise form.ValidationError("Name must be complete")
    return name