from django.shortcuts import render, get_object_or_404
from .models import Medicine
from django.http import HttpResponse

def home(request):
    # Default to showing all medicines if no filter is applied
    medicines = Medicine.objects.all()

    # Debugging: Print all medicines initially
    print("All medicines:", medicines)

    # Get the search query from the URL (e.g., /?q=cough)
    search_query = request.GET.get('q', '')  # 'q' is the search parameter from the form
    print("Search query:", search_query)

    if search_query:
        # Filter by name (case-insensitive)
        medicines = medicines.filter(name__icontains=search_query)
        # Debugging: Print medicines after applying the search filter
        print(f"Medicines after search filter for '{search_query}':", medicines)
    
    # Pass the medicines and search_query to the template
    return render(request, 'home.html', {'medicines': medicines, 'search_query': search_query})

def medicine_detail(request, pk):
    # Fetch the medicine with the given primary key (pk) or return 404 if not found
    medicine = get_object_or_404(Medicine, pk=pk)
    
    # Debugging: Print the medicine details that are being passed to the template
    print("Medicine details:", medicine)

    # Render the 'medicine_detail.html' template with the medicine data
    return render(request, 'catalog/medicine_detail.html', {'medicine': medicine})
