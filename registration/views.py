from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Home page - Requires login
@login_required
def homePage(request):
    return render(request, 'notes_upload/templates/notes_upload/home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname1 = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if User.objects.filter(username=uname1).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return redirect('/')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('/')

        # Create the user
        my_user = User.objects.create_user(uname1, email, pass1)
        my_user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('/login/')
        
    return render(request, 'registration/register1.html')

def LoginPage(request):
    if request.method == 'POST':
        username2 = request.POST.get('username')
        pass1 = request.POST.get('pass')

        user = authenticate(request, username=username2, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, "Username or password is incorrect.")
            return redirect('/login/')

    return render(request, 'registration/login1.html')

def logout_view(request):
    logout(request)
    return redirect('login')
