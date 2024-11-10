from django.shortcuts import render

# Create your views here.
def team(request):
    context = {}
    return render(request, "team.html", context)