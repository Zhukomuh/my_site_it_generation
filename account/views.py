from django.shortcuts import render
from .forms import UserRegistration

# Create your views here.
def registration_view(request):
    form = UserRegistration(request.POST or None)
    if form.is_valid():
        pass
    return render(request)
