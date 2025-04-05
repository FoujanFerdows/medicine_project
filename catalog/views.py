from django.shortcuts import render, get_object_or_404
from .models import Medicine

# Home view to display all medicines or search results
def home(request):
    # Default to showing all medicines if no filter is applied
    medicines = Medicine.objects.all()
    search_query = request.GET.get('q', '')  # Get the search query from the URL

    # If there's a search query, filter the medicines by name
    if search_query:
        medicines = medicines.filter(name__icontains=search_query)

    # Render the 'catalog/home.html' template with the medicines and search query
    return render(request, 'catalog/home.html', {
        'medicines': medicines,
        'search_query': search_query
    })

# Medicine detail view to display individual medicine information
def medicine_detail(request, pk):
    # Fetch the medicine with the given primary key (pk) or return 404 if not found
    medicine = get_object_or_404(Medicine, pk=pk)
    
    # Render the 'catalog/medicine_detail.html' template with the medicine data
    return render(request, 'catalog/medicine_detail.html', {'medicine': medicine})

# About page view
def about(request):
    return render(request, 'catalog/about.html')
