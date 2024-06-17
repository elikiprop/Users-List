from django.urls import path
from . import views  # Importing the views module from the current directory
from django.contrib.auth.views import LoginView  # Import LoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('landing/', views.landing_page, name='landing'),
    path('members/', views.member_list, name='member_list'),  # Add this line to map the URL to the member_list view function
]
