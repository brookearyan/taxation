from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import UserInfo

def index(request):
    latest_salary_list = UserInfo.objects.order_by('salary')
    template = loader.get_template('brackets/index.html')
    context = {
        'latest_salary_list': latest_salary_list,
    }
    return HttpResponse(template.render(context, request))

def display(request, user_info_id):
    user_info = get_object_or_404(UserInfo, pk=user_info_id)
    return render(request, 'brackets/display.html', {'user_info': user_info})
