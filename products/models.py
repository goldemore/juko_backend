from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from tinymce.models import HTMLField
from categories.models import Category



# Create your models here.

from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from tinymce.models import HTMLField
from categories.models import Category

class Product(TranslatableModel):
    title = models.CharField(max_length=250)
    products_code = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    tech_img = models.ImageField(upload_to='product_tech_img', null=True, blank=True)
    tech_img_pro = models.ImageField(upload_to='product_tech_img', null=True, blank=True)
    tech_img_pro2 = models.ImageField(upload_to='product_tech_img', null=True, blank=True)
    scope_of_using_img = models.ImageField(upload_to='scope_of_using', null=True, blank=True)

    translations = TranslatedFields(
        short_description = models.TextField(),
        tech_desc = HTMLField(),
        h2_title = models.CharField(max_length=250),
        h3_title = models.CharField(max_length=250),
        boot_description_title = models.CharField(max_length=250, default='N/A'),
        boot_description = models.TextField(default='N/A') 
    )

    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="product_images/")
 
    def __str__(self):
        return f"Image for {self.product.title}"
    







