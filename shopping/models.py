from django.db import models

# Create your models here.
class Products(models.Model):

    """
    Model to represent products in the LetsShop store.

    Attributes:
        question_text (CharField): The name or description of the product.
        price (DecimalField): The price of the product.
        image (ImageField): The image associated with the product.
    """

    question_text = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='products/', default= 1)
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    """
    Model to represent choices or store locations for a product.

    Attributes:
        question (ForeignKey): The product associated with the choice.
        choice_text (CharField): The name or description of the choice (store location).
        votes (IntegerField): The number of votes or reservations for this choice.
    """
    question = models.ForeignKey(Products, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text