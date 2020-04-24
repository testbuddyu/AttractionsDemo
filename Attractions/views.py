from django.shortcuts import render
from FirstPage.models import *


# Create your views here.


def page_attraction_anonymous(request, id=1):
    return render(request, "pageAttractionAnonymous.html", {'attraction': Attractions.objects.get(id=id)})


def page_attraction_ap(request):
    return render(request, "pageAttractionAP.html")


def page_attraction_moderation(request):
    return render(request, "pageAttractionForModeration.html")
