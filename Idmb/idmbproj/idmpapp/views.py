from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Avg, Max, Min, Sum
from .models import *
from .forms import MovieForm, ArtistForm, AwardForm, RatingForm, SearchForm
import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def index(request):
    """

    """
    form = MovieForm()
    if request.method == 'POST':
        add_movie = MovieForm(request.POST)
        if add_movie.is_valid():
            add_movie.save()
            return render(request, 'idmpapp/index.html', {'form': form})
    return render(request, 'idmpapp/index.html', {'form': form})


def artist(request):
    """

    """
    form = ArtistForm
    if request.method == 'POST':
        add_artist = ArtistForm(request.POST)
        if add_artist.is_valid():
            add_artist.save()
            return render(request, 'idmpapp/artist.html', {'form': form})
    return render(request, 'idmpapp/artist.html', {'form': form})


def award(request):
    """

    """
    form = AwardForm
    if request.method == 'POST':
        add_award = AwardForm(request.POST)
        if add_award.is_valid():
            add_award.save()
            return render(request, 'idmpapp/award.html', {'form': form})
    return render(request, 'idmpapp/award.html', {'form': form})


def rating(request):
    """

    """
    if request.method == "POST":
        rate_form = RatingForm(request.POST)
        # print(type(rate_form))
        if rate_form.is_valid():
            form_object = rate_form.save(commit=False)
            form_object.movie = rate_form.cleaned_data.get('movie')
            form_object.rating = rate_form.cleaned_data['rating']
            filtered_data = Rating.objects.filter(
                movie=form_object.movie, rating=form_object.rating)
            if filtered_data.count() >= 1:
                rate_obj = filtered_data.get()
                rate_obj.votes += 1
                rate_obj.save()
            # set_avg_rating(form_object.movie)
            else:
                form_object.votes = 1
                form_object.save()
                form_object.movie.save()
            # set_avg_rating(form_object.movie)
            movie = Movie.objects.get(name=form_object.movie)
            rating_obj = Rating.objects.filter(movie=movie)
            rating_list = [int(rating_data.votes)*int(rating_data.rating)
                            for rating_data in rating_obj]
            vote_list = [rating_data.votes for rating_data in rating_obj]
            movie.avg_rating = sum(rating_list)/sum(vote_list)
            movie.save()
            messages.success(request, "Rated Successfully !")
            # TODO -> Average rating Logic
            return redirect(reverse('rating'))
        else:
            messages.error(request, "Error While Rating ")
            return redirect(reverse('rating'))
    else:
        rate_form = RatingForm()
        context = {'form': rate_form}
        return render(request, 'idmpapp/index.html', context)


def avg1(request):
    """

    """
    a = Rating.objects.all().aggregate(Avg('rating'))
    print(a)
    return HttpResponse(a['rating__avg'])


def topten(req):
    movies = Movie.objects.all().order_by('-avg_rating')[:5]
    return render(req, 'idmpapp/display.html', {"context": movies})


def leastten(req):
    movies = Movie.objects.all().order_by('avg_rating')[:5]
    return render(req, 'idmpapp/display.html', {"context": movies})


def within(req):
    if req.POST:
        # breakpoint()
        # print(req.GET['startdate'])
        start_date = req.POST['startdate']
        end_date = req.POST['enddate']
        print(start_date,end_date)
        movies = Movie.objects.filter(Release_date__range=[start_date, end_date])
        return render(req, 'idmpapp/display.html', {"context": movies, "title": f'Search from {start_date} to {end_date}'})


def search_results(request):
  # breakpoint()
    form = SearchForm(request.POST or None)
    queryset = None
    if request.method == 'POST':
        queryset = Movie.objects.filter(name__icontains=form['name'].value(
        )) or Movie.objects.filter(artists__name=form['name'].value())

        print(queryset)
    context = {
        "form": form,
        "queryset": queryset}
    return render(request, 'idmpapp/details.html', context)
