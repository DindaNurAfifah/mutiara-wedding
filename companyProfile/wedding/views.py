from django.shortcuts import render
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    context = {
        'MEDIA_URL': settings.MEDIA_URL
    }
    return render(request, 'contact_us/contact.html', context)

def team_view(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'card_team' : [
            {"name" : "Anandiaz Agung Pradana", "Position" : "Leader", 'image' : 'anan.png'},
            {"name" : "Ryan Jusniansyah", "Position" : "Vice Leader", "image" : "aku.png"},
            {"name" : "Dinda Nur Afifah", "Position" : "Member 1", "image" : "Mbadinda.png"},
            {"name" : "Rafly Genta Pratama", "Position" : "Member 2", "image" : "Genta.png"},
            {"name" : "Gusti Dimas Novarossi", "Position" : "Member 3", "image" : "Banggusti.png"}
        ]
    }
    return render(request, 'team/team.html', context)

def home_view(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL
    }
    return render(request, 'homepage/homepage.html', context)

def about_view(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL
    }
    return render(request, 'about_us/about.html', context)

def services_view(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'cards': [
            {'title': 'Full Wedding Planning', 'description': 'Complete planning from start to finish, covering every detail so you can enjoy a stress-free experience.', 'image': 'card1.png', 'link': 'contact'},
            {'title': 'Day-of Coordination', 'description': 'We manage everything on the big day, ensuring smooth execution so you can focus on enjoying each moment.', 'image': 'card2.png', 'link': 'contact'},
            {'title': 'Design & Styling', 'description': 'Bringing your vision to life with personalized decor and ambiance that captures your love story.', 'image': 'card3.png', 'link': 'contact'},
            {'title': 'Destination Wedding Planning', 'description': 'Expertly coordinated weddings in beautiful locations, managing all logistics for a seamless celebration.', 'image': 'card4.png', 'link': 'contact'},   
            {'title': 'Elopement Planning', 'description': 'Intimate, personalized planning for couples seeking a stress-free, memorable elopement experience.', 'image': 'card5.png', 'link': 'contact'},   
            {'title': 'Vendor Sourcing & Management', 'description': 'Connecting you with trusted vendors and managing all coordination for a worry-free wedding day.', 'image': 'card6.png', 'link': 'contact'},   
        ]
    }
    return render(request, 'services/services.html', context)
