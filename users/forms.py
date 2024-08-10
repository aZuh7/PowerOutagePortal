from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

'''
The UserRegistrationForm class is a form class that inherits from Django's built-in
UserCreationForm class.

The class stores the fields defined in the User model in the Meta class.
'''
class UserRegistrationForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'zip', 'password1', 'password2']

'''
The LoginForm class is a form class that inherits from Django's built-in
AuthenticationForm class.

The class stores the email and password fields, then cleans the data, and returns
the cleaned data to the view function.
'''
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        return cleaned_data
                               