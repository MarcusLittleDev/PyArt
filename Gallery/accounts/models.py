from django.db import models
from django.contrib import auth


# Create your models here.

class UserManager(auth.models.BaseUserManager):
    """Helps Django work with our custom user model"""

    def create_user(self, email, username, password):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, username, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class UserProfile(auth.models.AbstractBaseUser, auth.models.PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username