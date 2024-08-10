from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def register_user(request):
    # There are only two types of HTTP requests: GET and POST.
    # GET requests are used to retrieve information from the server.
    # POST requests are used to send data to the server.
    # With that being said, here we are checking if the request is a POST request.
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # This line creates a new user object but does not save it to the database, until all the fields are validated.
            user.set_password(form.cleaned_data['password1'])
            user.user_type = 'user'
            user.save() # This line saves the user object to the database.
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password) # This line authenticates the user with built-in Django authentication system.
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else: # If the request is not a POST request, then we will render a blank registration form from forms.py
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
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
    else: 
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    if request.user.user_type == 'admin':
        return redirect('admin_dashboard')
    else:
        return redirect('user_dashboard')
    
