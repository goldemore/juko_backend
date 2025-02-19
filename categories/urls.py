from django.urls import path
from .views import CategoryByLanguageView

urlpatterns = [
    path('categories/<str:language_code>/', CategoryByLanguageView.as_view(), name='categories_by_language')
]