from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom manager for User model
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, user_type='user', **extra_fields):
        if not email:
            raise ValueError('Please fill out the Email Field')
        email = self.normalize_email(email)
        # Removed 'username' from the model creation
        user = self.model(email=email, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, user_type='admin', **extra_fields)

# User model extending AbstractBaseUser
class User(AbstractBaseUser):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('user', 'User')
    ]

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25, unique=True)  # Ensure email is unique
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    zip = models.CharField(max_length=5)
    user_type = models.CharField(max_length=5, choices=USER_TYPES, default='user')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=125)

    objects = UserManager()  # Set the custom manager for the User model

    USERNAME_FIELD = 'email'  # Set email as the username field
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone', 'address', 'zip']  # Required fields

    def __str__(self):
        return self.username
