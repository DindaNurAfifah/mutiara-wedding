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
        'MEDIA_URL': settings.MEDIA_URL
    }
    return render(request, 'team/team.html', context)

def services_view(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'cards': [
            {'title': 'Full Wedding Planning', 'description': 'Complete planning from start to finish, covering every detail so you can enjoy a stress-free experience.', 'image': 'card1.png', 'link': '#'},
            {'title': 'Day-of Coordination', 'description': 'We manage everything on the big day, ensuring smooth execution so you can focus on enjoying each moment.', 'image': 'card2.png', 'link': '#'},
            {'title': 'Design & Styling', 'description': 'Bringing your vision to life with personalized decor and ambiance that captures your love story.', 'image': 'card3.png', 'link': '#'},
            {'title': 'Destination Wedding Planning', 'description': 'Expertly coordinated weddings in beautiful locations, managing all logistics for a seamless celebration.', 'image': 'card4.png', 'link': '#'},   
            {'title': 'Elopement Planning', 'description': 'Intimate, personalized planning for couples seeking a stress-free, memorable elopement experience.', 'image': 'card5.png', 'link': '#'},   
            {'title': 'Vendor Sourcing & Management', 'description': 'Connecting you with trusted vendors and managing all coordination for a worry-free wedding day.', 'image': 'card6.png', 'link': '#'},   
        ]
    }
    return render(request, 'services/services.html', context)
