from django.urls import path
from .views import ProductDetailView, ProductListByCategoryView

urlpatterns = [
    path('product/<int:product_id>/<str:language_code>/',
         ProductDetailView.as_view(), name='product_by_language'),

    path('product-by-category/<int:category_id>/',
         ProductListByCategoryView.as_view(), name='product_by_category')
]
