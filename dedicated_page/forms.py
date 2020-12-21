from django import forms
from .models import Post

class customForm(forms.Form):
    content = forms.CharField(required=False)
    pk = forms.IntegerField(required=False)
