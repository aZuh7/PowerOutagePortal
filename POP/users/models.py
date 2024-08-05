from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager): # This class is used to create a custom user model as opposed to using Dango's built-in User model.
    def create_user(self, email, username, password=None, user_type='user', **extra_fields): # This method is used to create a new user.
        if not email: # This line checks if the email field is empty. If it is, then it tells the browser to raise a ValueError.
            raise ValueError('Please fill out the Email Field')
        email = self.normalize_email(email) # This line normalizes the email field by converting all characters to lowercase.
        user = self.model(email=email, username=username, user_type=user_type, **extra_fields) # This line creates a new user object.
        user.set_password(password) # This line sets the password for the user object.
        user.save(using=self._db) # This line saves the user object to the database.
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields): # This method is used to create a superuser.
        extra_fields.setdefault('is_admin', True) # This line sets the is_admin field to True.
        extra_fields.setdefault('is_staff', True) # This line sets the is_staff field to True.
        extra_fields.setdefault('is_superuser', True) # This line sets the is_superuser field to True.

        if extra_fields.get('is_admin') is not True: # This line checks if the is_admin field is not True. If it is not, then it tells the browser to raise a ValueError.
            raise ValueError('Superuser must have is_admin=True') 
        if extra_fields.get('is_staff') is not True: # This line checks if the is_staff field is not True. If it is not, then it tells the browser to raise a ValueError.
            raise ValueError('Superuser must have is_staff=True')
        
        return self.create_user(email, username, password, user_type='admin', **extra_fields) # This line creates a new superuser object.

class User(AbstractBaseUser, PermissionsMixin): # This is our custom User Model. It inherits from AbstractBaseUser and PermissionsMixin, which are built-in Django classes.
    USER_TYPES = [
        ('admin', 'Admin'),
        ('user', 'User')
    ]

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25, unique=True)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    zip = models.CharField(max_length=5)
    user_type = models.CharField(max_length=5, choices=USER_TYPES, default='user')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=125)

    objects = UserManager() # This tells Django to use UserManager as the default manager for this custom user model.

    USERNAME_FIELD = 'email' # This line tells Django to use the email field as the username field.
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone', 'address', 'zip'] # This line tells Django to require these fields when creating a new user.

    def __str__(self):
        return self.username

