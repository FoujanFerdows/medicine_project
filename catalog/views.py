# views.py

from django.shortcuts import render
from .models import Medicine  # Assuming you have a Medicine model

# Home view
def home(request):
    return render(request, 'home.html')

# Medicine detail view
def medicine_detail(request, pk):
    try:
        # Get the Medicine object based on the primary key
        medicine = Medicine.objects.get(pk=pk)
    except Medicine.DoesNotExist:
        # Handle the case where no medicine is found
        return render(request, 'medicine_not_found.html')

    return render(request, 'medicine_detail.html', {'medicine': medicine})


