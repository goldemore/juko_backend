from django.db import models

# Create your models here.


class ContactRequest(models.Model):
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    comment = models.TextField(blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)

  

