from django.db import models

# Create your models here.
class Products(models.Model):
    question_text = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='products/', default= 1)
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Products, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text