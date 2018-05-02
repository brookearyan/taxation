from django.http import HttpResponse

def index(request):
    return HttpResponse("HEY GURL HEYYYs")

def display(request, user_info_id):
    return HttpResponse("This is user number: %s" % user_info_id)
