from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Article(models.Model):
    title = models.CharField(max_length=255)

    content = CKEditor5Field(
        'Text',
        config_name='extends'
    )

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title