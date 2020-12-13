from django import forms
from .models import Post

class customForm(forms.Form):
    content = forms.CharField(required=False)
    pk = forms.IntegerField(required=False)


class PostForm(forms.ModelForm):
    pk = forms.IntegerField(required=False)
    class Meta:
        model = Post
        fields = '__all__'