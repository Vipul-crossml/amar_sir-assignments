from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("IDMB")

def detail(request, movie_id):
    return HttpResponse("You're looking at movie %s." % movie_id)

def results(request, movie_id):
    response = "You're looking at the results of ratings %s."
    return HttpResponse(response % movie_id)

def response(request, movie_id):
    return HttpResponse("You're voting on movie %s." % movie_id)