from django.urls import path

from . import views

app_name = 'brackets'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_info_id>/', views.display, name='display'),
    path('new/', views.new, name='new'),
]
