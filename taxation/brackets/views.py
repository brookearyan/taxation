from django.http import HttpResponse
from django.template import loader
from .models import UserInfo

def index(request):
    latest_salary_list = UserInfo.objects.order_by('salary')
    template = loader.get_template('brackets/index.html')
    context = {
        'latest_salary_list': latest_salary_list,
    }
    return HttpResponse(template.render(context, request))

def display(request, user_info_id):
    return HttpResponse("This is user number: %s" % user_info_id)
