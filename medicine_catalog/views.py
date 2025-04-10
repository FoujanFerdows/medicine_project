from django.shortcuts import render, get_object_or_404
from catalog.models import Medicine  # Import Medicine model

def home(request):
    # Default to showing all medicines if no filter is applied
    medicines = Medicine.objects.all()
    
    # Search filter by name (if provided)
    search_query = request.GET.get('q', '')  # Search query comes from the URL, e.g., /?q=cough
    if search_query:
        medicines = medicines.filter(name__icontains=search_query)  # Filter medicines by name

    # Category filter (if provided)
    category_filter = request.GET.get('category', '')
    if category_filter:
        medicines = medicines.filter(category__icontains=category_filter)  # Filter by category

    return render(request, 'home.html', {'medicines': medicines, 'search_query': search_query})

def medicine_detail(request, pk):
    # Fetch the medicine with the given primary key (pk) or return 404 if not found
    medicine = get_object_or_404(Medicine, pk=pk)

    # Render the 'medicine_detail.html' template with the medicine data
    return render(request, 'catalog/medicine_detail.html', {'medicine': medicine})
