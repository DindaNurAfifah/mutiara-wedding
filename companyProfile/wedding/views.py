from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

def contact_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject=subject,
                message=full_message,
                from_email=email,  # Sender's email
                recipient_list=["akabanelay@gmail.com"],  # List of recipients
                fail_silently=False,
            )
            messages.success(request, "Your email was sent successfully!")
        except Exception as e:
            messages.error(request, "Failed to send email. Please try again.")

        return redirect("/contact")
    
    context = {
        "MEDIA_URL": settings.MEDIA_URL,
        "active_page": "contact",
    }
    return render(request, "contact_us/contact.html", context)


def team_view(request):
    context = {
        "MEDIA_URL": settings.MEDIA_URL,
        "active_page": "team",
        "card_team": [
            {"name": "Anandiaz Agung Pradana", "Position": "Leader", "image": "anan.png"},
            {"name": "Ryan Jusniansyah", "Position": "Vice Leader", "image": "aku.png"},
            {"name": "Dinda Nur Afifah", "Position": "Member 1", "image": "Mbadinda.png"},
            {"name": "Rafly Genta Pratama", "Position": "Member 2", "image": "Genta.png"},
            {"name": "Gusti Dimas Novarossi", "Position": "Member 3", "image": "Banggusti.png"},
        ],
    }
    return render(request, "team/team.html", context)


def home_view(request):
    context = {
        "MEDIA_URL": settings.MEDIA_URL,
        "active_page": "homepage",
    }
    return render(request, "homepage/homepage.html", context)


def about_view(request):
    context = {
        "MEDIA_URL": settings.MEDIA_URL,
        "active_page": "about",
    }
    return render(request, "about_us/about.html", context)


def gallery_view(request):
    context = {
        "MEDIA_URL": settings.MEDIA_URL,
        "active_page": "gallery",
        "images": [
            {"url": "gallery1.png"},
            {"url": "gallery2.png"},
            {"url": "gallery3.png"},
            {"url": "gallery4.png"},
            {"url": "gallery5.png"},
            {"url": "gallery6.png"},
            {"url": "gallery7.png"},
            {"url": "gallery8.png"},
            {"url": "gallery9.png"},
            {"url": "gallery10.png"},
            {"url": "gallery11.png"},
            {"url": "gallery12.png"},
            {"url": "gallery13.png"},
            {"url": "gallery14.png"},
            {"url": "gallery15.png"},
            {"url": "gallery16.png"},
            {"url": "gallery17.png"},
            {"url": "gallery18.png"},
        ],
    }
    return render(request, "gallery/gallery.html", context)


def services_view(request):
    context = {
        "MEDIA_URL": settings.MEDIA_URL,
        "active_page": "services",
        "cards": [
            {
                "title": "Full Wedding Planning",
                "description": "Complete planning from start to finish, covering every detail so you can enjoy a stress-free experience.",
                "image": "card1.png",
                "link": "/contact",
                "cardDescription": "From the initial stages of brainstorming ideas to the final moments of your wedding day, we handle every detail. We assist in selecting the perfect venue, curating a list of reliable vendors, and developing a detailed timeline to ensure nothing is overlooked. Our team manages all communications and logistics, allowing you to relax and focus on creating lifelong memories with your loved ones. Think of us as your partners in crafting a seamless, personalized, and unforgettable wedding experience.",
            },
            {
                "title": "Day-of Coordination",
                "description": "We manage everything on the big day, ensuring smooth execution so you can focus on enjoying each moment.",
                "image": "card2.png",
                "link": "/contact",
                "cardDescription": "For couples who have already done the planning but want to ensure everything goes according to schedule, our day-of coordination service is ideal. We step in to review your plans, confirm vendor arrangements, and create a detailed timeline for the day. On the wedding day, we oversee the setup, direct vendors, and ensure every event flows smoothly. This allows you, your family, and your friends to relax and immerse yourselves in the joy of the celebration without worrying about logistics.",
            },
            {
                "title": "Design & Styling",
                "description": "Bringing your vision to life with personalized decor and ambiance that captures your love story.",
                "image": "card3.png",
                "link": "/contact",
                "cardDescription": "Your wedding design should be as unique as your love story. We work closely with you to develop a cohesive aesthetic that reflects your personality and vision. From selecting the perfect color palette and table settings to coordinating floral arrangements and lighting, every detail is meticulously planned. Our goal is to transform your venue into a breathtaking space that leaves a lasting impression on you and your guests, capturing the beauty and essence of your celebration.",
            },
            {
                "title": "Destination Wedding Planning",
                "description": "Expertly coordinated weddings in beautiful locations, managing all logistics for a seamless celebration.",
                "image": "card4.png",
                "link": "/contact",
                "cardDescription": "Planning a destination wedding can be overwhelming, but our expert team simplifies the process. We help you choose a stunning location, handle travel arrangements for you and your guests, and coordinate with local vendors to ensure every detail is perfect. From legal requirements to managing time zone challenges, we take care of it all. Our goal is to create a stress-free experience that allows you to celebrate your love story in a picturesque setting, no matter the distance.",
            },
            {
                "title": "Elopement Planning",
                "description": "Intimate, personalized planning for couples seeking a stress-free, memorable elopement experience.",
                "image": "card5.png",
                "link": "/contact",
                "cardDescription": "Elopements are about intimacy and authenticity, and we help you create a celebration that’s uniquely yours. From scouting breathtaking locations and arranging travel to booking a photographer and crafting a personalized ceremony, we handle every detail. Whether you dream of saying your vows on a mountaintop or a secluded beach, we make it happen effortlessly. Our planning ensures your elopement is as meaningful as a traditional wedding but without the stress of managing a larger event.",
            },
            {
                "title": "Vendor Sourcing & Management",
                "description": "Connecting you with trusted vendors and managing all coordination for a worry-free wedding day.",
                "image": "card6.png",
                "link": "/contact",
                "cardDescription": "Finding the right vendors can be a daunting task, but our expertise makes it simple. We carefully curate a list of reliable professionals who match your style, budget, and preferences. From florists and photographers to caterers and musicians, we coordinate every detail, ensuring they work seamlessly together. Our team oversees contracts, payments, and timelines, leaving no room for errors. On your wedding day, we manage all vendor interactions, so you can focus on celebrating with your loved ones.",
            },
        ],
    }
    return render(request, "services/services.html", context)
