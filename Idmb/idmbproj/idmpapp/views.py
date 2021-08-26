from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Avg, Max, Min, Sum
from .models import *
from .forms import MovieForm, ArtistForm, AwardForm, RatingForm

# Create your views here.

def index(request):
    """
    
    """
    form = MovieForm()
    if request.method=='POST':
        add_movie=MovieForm(request.POST)
        if add_movie.is_valid():
            add_movie.save()
            return render(request,'idmpapp/index.html',{'form':form})
    return render(request,'idmpapp/index.html',{'form':form})

def artist(request):
    """
    
    """
    form=ArtistForm
    if request.method=='POST':
        add_artist=ArtistForm(request.POST)
        if add_artist.is_valid():
            add_artist.save()
            return render(request,'idmpapp/artist.html',{'form':form})
    return render(request,'idmpapp/artist.html',{'form':form})

def award(request):
    """

    """
    form=AwardForm
    if request.method=='POST':
        add_award=AwardForm(request.POST)
        if add_award.is_valid():
            add_award.save()
            return render(request,'idmpapp/award.html',{'form':form})
    return render(request,'idmpapp/award.html',{'form':form})

def rating(request):
    """

    """
    form=RatingForm
    title="Add Rating"
    if request.method=='POST':
        add_rating=RatingForm(request.POST)
        if add_rating.is_valid():
            add_rating.save()
            return render(request,'idmpapp/rating.html',{'form':form,'title': title})
    return render(request,'idmpapp/rating.html',{'form':form})

def avg1(request):
    """

    """
    a=Rating.objects.all().aggregate(Avg('rating'))
    print(a)
    return HttpResponse(a['rating__avg'])


