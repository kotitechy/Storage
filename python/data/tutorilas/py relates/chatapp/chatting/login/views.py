from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.


class Signupform(UserCreationForm):
    class Meta:
        model = User
        fileds = ['username', 'password', 'phno']



def login(request):

    return render(request, 'lpg.html')