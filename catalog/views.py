from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicine, Symptom, ShoppingList  # Import Symptom model for symptom search

# Home view to display all medicines or search results
def home(request):
    # Fetch all medicines and symptoms by default
    medicines = Medicine.objects.all()
    symptoms = Symptom.objects.all()  # Fetch all symptoms by default

    # Get the search query, letter, and search type from the URL
    search_query = request.GET.get('q', '')
    letter = request.GET.get('letter', '')  # New 'letter' parameter to filter by letter
    search_type = request.GET.get('search_type', 'medicine')  # Default to medicine search

    # Filter by search query if available
    if search_query:
        if search_type == 'medicine':
            medicines = medicines.filter(name__icontains=search_query)
        elif search_type == 'symptom':
            symptoms = symptoms.filter(name__icontains=search_query)

    # Filter by letter if selected (only for medicine)
    if letter:
        medicines = medicines.filter(name__istartswith=letter)

    # Get the list of unique first letters for the alphabetical filter
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    return render(request, 'catalog/home.html', {
        'medicines': medicines,
        'symptoms': symptoms,
        'search_query': search_query,
        'alphabet': alphabet,  # Pass the alphabet list to the template
        'letter': letter,      # Pass the selected letter for active highlighting
        'search_type': search_type,  # Pass the search type (medicine or symptom)
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
    return render(request, 'catalog/login.html')

from django.contrib.auth.forms import UserCreationForm  # Add this import at the top with the others

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'catalog/signup.html', {'form': form})
