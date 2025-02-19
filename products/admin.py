from django.contrib import admin
from .models import Product, ProductImage
from parler.admin import TranslatableAdmin
from django.utils.html import format_html


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5
    fields = (
        "image",
        "image_preview",
    )
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        """Returns the HTML for the image preview."""
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 150px; height: auto;" />', obj.image.url
            )
        return "No image"

    image_preview.short_description = "Preview"


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    inlines = [ProductImageInline]
    list_display = ('title', 'category_name', 'first_image_preview', )
    list_per_page = 10
    search_fields = ['title']


    fieldsets = (
        ('Header Product', {'fields': ('title', 'short_description',
         'tech_desc', 'tech_img', 'products_code', 'category')}),
        ('After Header', {'fields': ('h2_title', 'h3_title', 'tech_img_pro', 'tech_img_pro2',
         'boot_description_title', 'boot_description', 'scope_of_using_img')})
    )

    def category_name(self, obj):
        return obj.category.title
    category_name.short_description = 'Category'

    def first_image_preview(self, obj):
        """Returns the preview of the first image uploaded for the product."""
        first_image = obj.images.first()  # Get the first related ProductImage
        if first_image and first_image.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: auto;" />', first_image.image.url
            )
        return "No image"

    first_image_preview.short_description = "First Image"
