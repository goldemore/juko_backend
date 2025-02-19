from django.shortcuts import render
from .models import Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer


# Create your views here.

SUPPORTED_LANGUAGE_CODES = ["en", "ru", "ka"]


class CategoryByLanguageView(APIView):
    def get(self, request, language_code):
        if language_code not in SUPPORTED_LANGUAGE_CODES:
            return Response({"error": f"Unsupported language: {language_code}"}, status=status.HTTP_400_BAD_REQUEST)

        categories = Category.objects.language(
            language_code).all().order_by("id")
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)
