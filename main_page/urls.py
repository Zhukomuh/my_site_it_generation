from .views import main, update_reservation, list_reservations
from django.urls import path

app_name = 'main_page'

urlpatterns = [
    path('manager/update_reserve/<int:pk>', update_reservation, name='update_reservation'),
    path('', main),
    path('manager/reserve_list', list_reservations, name='list_reservations'),
]
