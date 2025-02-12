
from django.shortcuts import render, get_object_or_404
from .models import Medicine

# Home view
def home(request):
    return HttpResponse("<h1>Welcome to the Medicine App!</h1>")

# Medicine detail view
def medicine_detail(request, pk):
    # Get the Medicine object or return 404 if not found
    medicine = get_object_or_404(Medicine, pk=pk)
    
    # Render the medicine detail template with the medicine object
    return render(request, 'medicine_detail.html', {'medicine': medicine})
