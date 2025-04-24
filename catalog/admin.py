from django.contrib import admin
from catalog.models import Medicine, Category, Symptom  
from .models import ContactSubmission
from .models import Profile

admin.site.register(Medicine)
admin.site.register(Category)
admin.site.register(Symptom) 
@admin.register(ContactSubmission)

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'submitted_at')
    list_filter  = ('submitted_at',)
    search_fields = ('title', 'email', 'description') 

class ProfileAdmin(admin.ModelAdmin):
    list_display   = ('user', 'phone', 'updated_at')
    search_fields  = ('user__username', 'user__email', 'phone')
