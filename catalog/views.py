from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicine, Symptom, MedicineList, ContactSubmission
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm

from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts           import render, redirect
from django.contrib.auth        import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views  import PasswordChangeView
from django.urls                import reverse_lazy
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm

def landing(request):
    return render(request, 'catalog/landing.html')


def home(request):
    print("⮕ home() GET:", dict(request.GET))
    medicines = Medicine.objects.all().prefetch_related('symptoms') 

    search_query = request.GET.get('q', '')
    letter = request.GET.get('letter', '')  
    search_type = request.GET.get('search_type', 'medicine')  

    if letter:
        medicines = medicines.filter(name__istartswith=letter)

    elif search_query:
        if search_type == 'medicine':
            medicines = medicines.filter(name__icontains=search_query)
        else:  
            medicines = (
                medicines
                .filter(symptoms__name__icontains=search_query)
                .distinct()
            )

    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    return render(request, 'catalog/home.html', {
        'medicines': medicines,
        'search_query': search_query,
        'alphabet': alphabet,  
        'letter': letter,      
        'search_type': search_type,  
    })


def medicine_detail(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'catalog/medicine_detail.html', {'medicine': medicine})


def add_to_medicine_list(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    ml, _ = MedicineList.objects.get_or_create(user=request.user)
    ml.medicines.add(medicine)
    return redirect(reverse_lazy('profile'))


def remove_from_medicine_list(request, medicine_id):
    ml, _ = MedicineList.objects.get_or_create(user=request.user)
    medicine = get_object_or_404(Medicine, id=medicine_id)
    ml.medicines.remove(medicine)
    return redirect('profile')
    

def about(request):
    return render(request, 'catalog/about.html')


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
    

def login_view(request):
    return render(request, 'catalog/login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)                   
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'catalog/signup.html', {'form': form})


@login_required
def profile(request):
    ml, _ = MedicineList.objects.get_or_create(user=request.user)
    meds = ml.medicines.all().order_by('category__name', 'name')
    return render(request, 'catalog/profile.html', {'medicine_list': ml, 'medicines': meds})


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
 
