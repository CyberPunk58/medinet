from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

        widgets = {
            'content': CKEditor5Widget(
                config_name='extends'
            )
        }