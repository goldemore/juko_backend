from django.urls import path
from .views import ContactRequestCreateView

urlpatterns = [
    path('send-client-mail/', ContactRequestCreateView.as_view({'post': 'create'}), name='Contact-request')
]