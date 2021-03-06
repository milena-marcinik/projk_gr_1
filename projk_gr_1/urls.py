"""projk_gr_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user_panel import views as user_views
from user_panel.views import UserListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manage_library.urls')),
    path('adduser/', user_views.add_user, name='add_user'),
    path('users/', UserListView.as_view(template_name='user_panel/users_all.html'), name='all_users'),
    path('login/', auth_views.LoginView.as_view(template_name='user_panel/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_panel/logout.html'), name='logout'),

]
