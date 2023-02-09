from django.shortcuts import render, redirect
from .models import Category, Dish, Events, About, PhotoGallery
from django.http import HttpResponse
from .forms import ReservationForm


# Create your views here.


def main(request):
    if request.method == 'POST':
        form_reserve = ReservationForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    events = Events.objects.filter(is_visible=True)
    about = About.objects.get()
    our_photo = PhotoGallery.objects.filter(is_visible=True)
    form_reserve = ReservationForm()

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'form_reserve': form_reserve,
        'events': events,
        'about': about,
        'our_photo': our_photo,

    })
