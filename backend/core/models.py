from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"
    
class Establishment(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20)
    address=models.CharField(max_length=255)
    categories=models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name}"
    
class Promotion(models.Model):
    title=models.CharField(max_length=75)
    description=models.CharField(max_length=255)
    establishment=models.ForeignKey(Establishment,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

