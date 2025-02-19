from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.


class Category(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=250)
    )
    image = models.ImageField(upload_to='categories', null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.safe_translation_getter('title', language_code='en', any_language=True) or "Unnamed Category"
