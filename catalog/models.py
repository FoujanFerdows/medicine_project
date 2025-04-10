from django.db import models
from django.contrib.auth.models import User

AVAILABILITY_CHOICES = [
    ('in_stock', 'In Stock'),
    ('out_of_stock', 'Out of Stock'),
]

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    active_ingredients = models.TextField()
    usage_instructions = models.TextField()
    side_effects = models.TextField()

    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='in_stock')

    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# New Symptom model for symptom-based search
class Symptom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


# New ShoppingList model
class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Medicine)

    def __str__(self):
        return f"Shopping List for {self.user.username}"


    def __str__(self):
        return f"Shopping List for {self.user.username}"

