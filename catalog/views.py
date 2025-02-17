from django.shortcuts import render, get_object_or_404
from .models import Medicine


def home(request):
    return HttpResponse("<h1>Welcome to the Medicine App!</h1>")


def medicine_detail(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    

    return render(request, 'medicine_detail.html', {'medicine': medicine})


