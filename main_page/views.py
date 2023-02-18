from django.shortcuts import render, redirect
from .models import Category, Dish, Events, About, PhotoGallery, Chefs, WhyUs, Reservation
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ReservationForm


def is_manager(user):
    return user.groups.filter(name='manager').exists()


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
    # about = About.objects.get()
    our_photo = PhotoGallery.objects.filter(is_visible=True)
    form_reserve = ReservationForm()
    why_us = WhyUs.objects.filter(is_visible=True)
    chefs = Chefs.objects.filter(is_visible=True)

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'form_reserve': form_reserve,
        'events': events,
        'about': about,
        'our_photo': our_photo,
        'why_us': why_us,
        'chefs': chefs,

    })


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    Reservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('main_page:list_reservations')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def list_reservations(request):
    messages = Reservation.objects.filter(is_processed=False)
    return render(request, 'reservations.html', context={
        'reservations': messages
    })
