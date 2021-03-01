from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_manage_library, name="main_manage_library"),
]