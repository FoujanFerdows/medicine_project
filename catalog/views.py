from django.shortcuts import render
from .models import Medicine

# Home Page View (displays all medicines)
def home(request):
    medicines = Medicine.objects.all()  # Fetch all medicines from the database
    return render(request, 'home.html', {'medicines': medicines})

# Medicine Detail View (displays a single medicine's details)
def medicine_detail(request, pk):
    try:
        medicine = Medicine.objects.get(pk=pk)  # Fetch a single medicine by primary key
    except Medicine.DoesNotExist:
        medicine = None  # Handle case where medicine doesn't exist
    return render(request, 'medicine_detail.html', {'medicine': medicine})

