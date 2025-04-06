from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicine, ShoppingList  # Import ShoppingList model

# Home view to display all medicines or search results
def home(request):
    medicines = Medicine.objects.all()
    search_query = request.GET.get('q', '')  # Get the search query from the URL

    if search_query:
        medicines = medicines.filter(name__icontains=search_query)

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

# Add to shopping list view
def add_to_shopping_list(request, medicine_id):
    # Fetch the medicine object based on the provided ID
    medicine = get_object_or_404(Medicine, id=medicine_id)

    if request.user.is_authenticated:
        # Fetch the user's shopping list, or create one if it doesn't exist
        shopping_list, created = ShoppingList.objects.get_or_create(user=request.user)
        
        # Add the medicine to the shopping list
        shopping_list.medicines.add(medicine)
        
        # Save the shopping list
        shopping_list.save()

        # Redirect back to the medicine detail page after adding
        return redirect('medicine_detail', pk=medicine.id)
    else:
        # If the user is not authenticated, redirect them to the login page
        return redirect('login')  # Update this to your login URL name

# About page view
def about(request):
    return render(request, 'catalog/about.html')

# Contact page view
def contact(request):
    return render(request, 'catalog/contact.html')

# Login view (you can later add authentication logic here)
def login_view(request):
    return render(request, 'catalog/login.html')  # Render the login template
