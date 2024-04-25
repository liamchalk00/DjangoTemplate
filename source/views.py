import sys
import time

from django.shortcuts import render, HttpResponse, HttpResponseRedirect


def home(request):
    # return HttpResponse("Home page!")
    return render(request, "home.html", {})