from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """def create new user profile"""
        if not email:
            raise ValueError("User must have email address")
        email = self.normalize_email(email) #standarizes the case of the email for storage
        user = self.model(email=email, name=name) # creates a new model object for the specific user

        user.set_password(password) #keep pw stored as hash, not actual clear text
        user.save(using=self._db) # save data to db
        
        return user

    def create_superuser(self, email, name, password):
        """create super user with given details"""
        user = self.create_superuser(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfiles(AbstractBaseUser, PermissionsMixin):
    """Database model for userins in the system"""
    """Customize the default user model"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email' # change email field as the default
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(slef):
        """Retrieve short name"""
        return self.name

    def __str__(self):
        """Convert user profile object to a string"""
        """Return string representation of the user"""
        return self.email 