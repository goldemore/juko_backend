from rest_framework import serializers
from .models import Product, ProductImage



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage 
        fields = ["image"]

    def to_representation(self, obj):
        return obj.image.url if obj.image else None


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)


    class Meta:
        model = Product
        fields = ['id', 'title', 'short_description', 'tech_img', 'products_code', 'category', 'h2_title', 'h3_title', 'tech_img_pro', 'tech_img_pro2',
                  'boot_description_title', 'boot_description', 'scope_of_using_img','images']

class ProductListByCategorySerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'first_image', 'category_name']

    def get_first_image(self, obj):
        first_image = obj.images.first()
        return first_image.image.url if first_image else None
    
    def get_category_name(self, obj):

        return obj.category.safe_translation_getter('title', language_code='en', any_language=True)

    
    

  
