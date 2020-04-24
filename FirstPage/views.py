from django.shortcuts import render
from FirstPage.models import  *

def main_page_anonymous(request):
    return render(request, "mainpageAnonymous.html")


def main_page_ap(request):
    return render(request, "mainpageAP.html")


def page_create_request(request):
    return render(request, "pageCreateRequest.html")


def page_profile_ap(request):
    return render(request, "pageMyProfileAP.html")


def page_profile_manager(request):
    return render(request, "pageMyProfileManager.html")


def page_users_request(request):
    return render(request, "pageUsersRequests.html")
