from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_info_id>/', views.display, name='display'),
]
