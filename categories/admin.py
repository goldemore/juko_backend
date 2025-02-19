from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Category
from django.utils.html import format_html

# Register your models here.
@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('title', 'image_preview')
    readonly_fields = ('image_preview',)
    fieldsets = (
    (None, {'fields': ('title',)}),
    ('Category image', {'fields': ('image', 'image_preview')}),
)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: auto;" />',
                obj.image.url,
            )
        return "No image"


