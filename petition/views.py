from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Petition, Vote

@login_required
def petition_page(request):
    if request.method == "POST":
        if "new_petition" in request.POST:
            title = request.POST.get("title")
            image = request.FILES.get("image")  # 👈 capture uploaded file
            if title:
                Petition.objects.create(
                    title=title,
                    created_by=request.user,
                    image=image    # 👈 save uploaded file to model
                )
        elif "vote" in request.POST:
            petition_id = request.POST.get("petition_id")
            petition = Petition.objects.get(id=petition_id)
            Vote.objects.get_or_create(petition=petition, user=request.user)

    petitions = Petition.objects.all().order_by("-created_at")
    return render(request, "petition.html", {"petitions": petitions})

