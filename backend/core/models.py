from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Category(models.Model):
    name=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Establishment(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20)
    address=models.CharField(max_length=255)
    categories=models.ManyToManyField("Category")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="establishments"
    )

    def __str__(self):
        return f"{self.name}"
    
class Promotion(models.Model):
    title=models.CharField(max_length=75)
    description=models.CharField(max_length=255)
    establishment=models.ForeignKey(Establishment,on_delete=models.CASCADE, related_name="promotions")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="promotions"
    )


    def __str__(self):
        return f"{self.title}"

