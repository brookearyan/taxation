from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import UserInfo
from .forms import New

def index(request):
    latest_salary_list = UserInfo.objects.order_by('salary')
    template = loader.get_template('brackets/index.html')
    context = {
        'latest_salary_list': latest_salary_list,
    }
    return HttpResponse(template.render(context, request))
#fix so above is applicable to form...no more salary list.
def display(request, user_info_id):
    user_info = get_object_or_404(UserInfo, pk=user_info_id)
    return render(request, 'brackets/display.html', {'user_info': user_info})

def new(request):
    if request.method == 'POST':
        form = New(request.POST)
        if form.is_valid():
            zip_code = form.cleaned_data['zip_code']
            salary = form.cleaned_data['salary']
            marital_status = form.cleaned_data['marital_status']
    else:
        form = New()
        
    return render(request, 'brackets/new.html', {'form': form})
# def new(request):
#     if request.method == "POST":
#         form = New(request.POST)
#         if form.is_valid():
#             user_info = form.save(commit=False)
#             user_info.zip_code = request.zip_code
#             user_info.salary = request.salary
#             user_info.marital_status = request.marital_status
#             return redirect('display', pk=user_info.pk)
#     else:
#         form = New()
#     return render(request, 'brackets/new.html', {'form': form})
