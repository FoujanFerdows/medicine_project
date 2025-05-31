from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

AVAILABILITY_CHOICES = [
    ('in_stock', 'In Stock'),
    ('out_of_stock', 'Out of Stock'),
]

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"
    
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
    symptoms = models.ManyToManyField('Symptom', blank=True, related_name='medicines')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Symptom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class MedicineList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='medicine_lists')
    medicines = models.ManyToManyField('Medicine', blank=True, related_name='medicine_lists')
    
    def __str__(self):
        return f"Medicine List for {self.user.username}"


class ContactSubmission(models.Model):
    title       = models.CharField(max_length=150)
    description = models.TextField()
    email       = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} from {self.email}"


class Profile(models.Model):
    user           = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    health_status  = models.TextField(blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

