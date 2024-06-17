from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView  # Import LoginView

from users import views  # Assuming 'users' is your Django app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('landing/', views.landing_page, name='landing'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
