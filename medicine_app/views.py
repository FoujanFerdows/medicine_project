# views.py
from django.shortcuts import render
from .models import Medicine  # Make sure to import your model if needed

# Define the home view
def home(request):
    return render(request, 'home.html')

# Define the medicine_detail view
def medicine_detail(request, pk):
    medicine = Medicine.objects.get(pk=pk)  # Get the Medicine object with the given primary key (pk)
    return render(request, 'medicine_detail.html', {'medicine': medicine})
