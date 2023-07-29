from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.contrib import messages

# create and save user for custom user model
class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            return messages.error('the email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            return messages.error('superuser must have staff=true')
        if extra_fields.get('is_superuser') is not True:
            raise messages.error('superuser must have superuser=true')
        return self.create_user(email,password,**extra_fields )



# custom user model
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.email 