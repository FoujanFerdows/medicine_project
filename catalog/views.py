from django.shortcuts import render, get_object_or_404
from .models import Medicine

# Home view to display all medicines or search results
def home(request):
    medicines = Medicine.objects.all()
    search_query = request.GET.get('q', '')

    if search_query:
        medicines = medicines.filter(name__icontains=search_query)

    return render(request, 'catalog/home.html', {
        'medicines': medicines,
        'search_query': search_query
    })

# Medicine detail view
def medicine_detail(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'catalog/medicine_detail.html', {'medicine': medicine})

# About page view
def about(request):
    return render(request, 'catalog/about.html')
