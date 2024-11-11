from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
def team(request):
    context = {}
    return render(request, "team.html", context)
=======
def contact_view(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'contact_us/contact.html')
>>>>>>> 50c2b05d77617833c97528e9f82746332b9f9372
