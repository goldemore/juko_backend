from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    title_en = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'title_en',]

    def get_title_en(self, obj):
        return obj.safe_translation_getter('title', language_code='en', any_language=True)
    

