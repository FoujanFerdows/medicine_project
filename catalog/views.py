from django.shortcuts import render
from .models import Medicine

def home(request):
    medicines = Medicine.objects.all()  
    return render(request, 'home.html', {'medicines': medicines})

def medicine_detail(request, pk):
    medicine = Medicine.objects.get(pk=pk)
    return render(request, 'medicine_detail.html', {'medicine': medicine})
