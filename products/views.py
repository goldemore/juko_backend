from django.shortcuts import render
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, ProductListByCategorySerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


# Create your views here.

SUPPORTED_LANGUAGE_CODES = [
    "en",
    "ru",
    "ka",
]  # Define your supported languages here


class ProductDetailView(APIView):
    """
    API view to retrieve a single product by its ID and language code.
    """

    def get(self, request, product_id, language_code):
        # Validate the language code
        if language_code not in SUPPORTED_LANGUAGE_CODES:
            return Response({"error": f"Unsupported language: {language_code}"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the product by ID
            product = Product.objects.get(id=product_id)

            # Set the current language for the product
            product.set_current_language(language_code)

            # Serialize the product data
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )


class ProductListByCategoryView(generics.ListAPIView):
    """
    API view to list products by category.
    """
    serializer_class = ProductListByCategorySerializer

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        if category_id:
            return Product.objects.filter(category_id=category_id)
        return Product.objects.all()
