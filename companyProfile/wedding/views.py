from django.shortcuts import render

def contact_view(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'contact_us/contact.html')