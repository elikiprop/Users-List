from django.shortcuts import render, redirect # type: ignore
from django.contrib import messages # type: ignore
from .forms import UserRegisterForm  # Assuming you have this form in forms.py
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth.views import LoginView, LogoutView # type: ignore

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')  # Access email field from form
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def landing_page(request):
    # Fetch all users from the database
    users = User.objects.all()
    return render(request, 'users/landing.html', {'users': users})


def member_list(request):
    # Retrieve all users from the database
    members = User.objects.all()
    return render(request, 'users/member_list.html', {'members': members})