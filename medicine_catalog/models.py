from django.db import models

# you create your models here, like category model, medicine model, etc. 



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    active_ingredients = models.TextField()
    usage_instructions = models.TextField()
    side_effects = models.TextField()
    availability = models.CharField(max_length=50, choices=[('over_the_counter', 'Over-the-counter'), ('prescription', 'Prescription')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    symptoms = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class Prescription(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    prescription_document = models.FileField(upload_to='prescriptions/')
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.medicine.name} by {self.user.username}"
