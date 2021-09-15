from django import forms
from .models import UserArticle


class Userarticleform(forms.ModelForm):
    class Meta:
        model = UserArticle
        fields = ('title','author','content','image','source')

