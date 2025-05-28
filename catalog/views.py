from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicine, Symptom, ShoppingList  # Import Symptom model for symptom search
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
from .models import ContactSubmission

from django.shortcuts           import render, redirect
from django.contrib.auth        import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views  import PasswordChangeView
from django.urls                import reverse_lazy
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm

# Home view to display all medicines or search results
def home(request):
    print("⮕ home() GET:", dict(request.GET))
    # Fetch all medicines by default
    medicines = Medicine.objects.all().prefetch_related('symptoms') 

    # Get the search query, letter, and search type from the URL
    search_query = request.GET.get('q', '')
    letter = request.GET.get('letter', '')  # New 'letter' parameter to filter by letter
    search_type = request.GET.get('search_type', 'medicine')  # Default to medicine search

    # Filter by search query if available
    if letter:
        medicines = medicines.filter(name__istartswith=letter)

    # 2) Else if they entered text, filter by name or symptom
    elif search_query:
        if search_type == 'medicine':
            medicines = medicines.filter(name__icontains=search_query)
        else:  # search_type == 'symptom'
            medicines = (
                medicines
                .filter(symptoms__name__icontains=search_query)
                .distinct()
            )

    # Get the list of unique first letters for the alphabetical filter
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    return render(request, 'catalog/home.html', {
        'medicines': medicines,
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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ContactSubmission.objects.create(
                title       = cd['title'],
                description = cd['description'],
                email       = cd['email'],
            )
            send_mail(
                subject=f"[MediQuick] New Contact: {cd['title']}",
                message=(
                    f"New submission from {cd['email']}\n\n"
                    f"Title: {cd['title']}\n\n"
                    f"Message:\n{cd['description']}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return redirect('contact_thanks')
    else:
        form = ContactForm()
    return render(request, 'catalog/contact.html', {'form': form})

def contact_thanks(request):
    return render(request, 'catalog/contact_thanks.html')
    
# Login view (you can later add authentication logic here)
def login_view(request):
    return render(request, 'catalog/login.html')

from django.contrib.auth.forms import UserCreationForm  # Add this import at the top with the others

# Signup view

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)                   # optional: log them in immediately
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'catalog/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'catalog/profile.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'catalog/profile_edit.html', {
        'u_form': u_form,
        'p_form': p_form
    })

class MyPasswordChangeView(PasswordChangeView):
    template_name      = 'catalog/password_change.html'
    success_url        = reverse_lazy('profile')

