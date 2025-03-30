from django.shortcuts import render, get_object_or_404
from .models import Medicine

# Home view to display all medicines or search results
def home(request):
    # Default to showing all medicines if no filter is applied
    medicines = Medicine.objects.all()

    # Get the search query from the URL (e.g., /?q=cough)
    search_query = request.GET.get('q', '')  # 'q' is the search parameter from the form

    if search_query:
        # Filter by name (case-insensitive)
        medicines = medicines.filter(name__icontains=search_query)
    
    # Pass the medicines and search_query to the template
    return render(request, 'home.html', {'medicines': medicines, 'search_query': search_query})

# Medicine detail view to display individual medicine information
def medicine_detail(request, pk):
    # Fetch the medicine with the given primary key (pk) or return 404 if not found
    medicine = get_object_or_404(Medicine, pk=pk)
    
    # Render the 'medicine_detail.html' template with the medicine data
    return render(request, 'catalog/medicine_detail.html', {'medicine': medicine})

def about(request):
    return render(request, 'about.html')
