from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import UserInfo
from .forms import New

def index(request):
    return render(request, 'brackets/index.html')

def display(request, user_info_id):
    user_info = get_object_or_404(UserInfo, pk=user_info_id)
    return render(request, 'brackets/display.html', {'user_info': user_info})

def new(request):
    if request.method == 'POST':
        form = New(request.POST)
        if form.is_valid():
            user_info = form.cleaned_data
            zip_code = form.cleaned_data['zip_code']
            salary = form.cleaned_data['salary']
            marital_status = form.cleaned_data['marital_status']
    else:
        form = New()
        return render(request, 'brackets/new.html', {'form':form})

    return HttpResponseRedirect(reverse('brackets:display', {'user_info_id': user_info.pk}))
# current url path /brackets/new/form... needds to post to /user-info or /##
