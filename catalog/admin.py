from django.contrib import admin
from catalog.models import Medicine, Category, Symptom  # Import Symptom model

# Register your models
admin.site.register(Medicine)
admin.site.register(Category)
admin.site.register(Symptom)  # Register the Symptom model
