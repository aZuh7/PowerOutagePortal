from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.user_type = 'user'
            user.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email}, Password: {password}")  # Debugging line
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print("Authentication successful") # Debugging line
            login(request, user)
            return redirect('dashboard')
        else:
            print("Authentication failed.") # Debuggin line
            return render(request, 'users/login.html', {'error':'Invalid email or password.'})
    return render(request, 'users/login.html')

def logout_user(request):
    return redirect('home')

@login_required
def dashboard(request):
    print(f"User Type: {request.user.user_type}")  # Debugging line
    if request.user.user_type == 'admin':
        return redirect('admin_dashboard')
    else:
        return redirect('user_dashboard')
    
