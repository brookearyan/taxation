from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import UserInfo
from .forms import New
import coreapi

def index(request):
    if request.method == 'POST':
        form = New(request.POST)
        if form.is_valid():
            user_info = UserInfo(
                zip_code=form.cleaned_data['zip_code'],
                salary=form.cleaned_data['salary'],
                marital_status=form.cleaned_data['marital_status']
                )
            user_info.save()
        return HttpResponseRedirect(reverse('brackets:display', args=(user_info.id,)))

    else:
        form = New()
        return render(request, 'brackets/index.html', {'form':form})

def display(request, user_info_id):
    try:
        user_info = get_object_or_404(UserInfo, pk=user_info_id)
    except UserInfo.DoesNotExist:
        raise Http404("this user does not exist")
    return render(request, 'brackets/display.html', {'user_info': user_info})
    
# CAPITALIZE OR LOWERCASE?????
# add city & state to form to lowercase, bracket api hit to lowercase
# add local tax algo with array of city names
# federal & state tax algo logic --make sure is reuseable, do not use manual id's?
# find chart gem
# research allocation of new tax bill

#
# def city_and_state(zip_code):
#     zip_code = str(zip_code)
#     api_key = 'jYDPzTUAvlLWJMPe241qEXPVJKvIT83FLp5IBV9V7UxPu80KFCo7JyBzUqCoxdm3'
#     request_url = 'https://www.zipcodeapi.com/rest/'+ api_key + '/info.json/'+ zip_code +'/degrees'
#     client = coreapi.Client()
#     schema = client.get(request_url)
#     params = { city: 'city', state: 'state' }
#     result = client.action(schema, params)
#     return result
