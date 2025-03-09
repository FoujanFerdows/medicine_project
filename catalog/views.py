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
        print(f"Medicines after search filter for '{search_query}':", list(medicines))  # Convert QuerySet to list for easier reading
    
    # Pass the medicines and search_query to the template
    return render(request, 'home.html', {'medicines': medicines, 'search_query': search_query})

