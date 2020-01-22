from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an unique username")
        if not first_name:
            raise ValueError("Users pass in a first name")
        if not last_name:
            raise ValueError("Users pass in a last name")

        user = self.model(
                email=self.normalize_email(email),
                username=username,
                first_name=first_name,
                last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        user = self.create_user(
                email,
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Profile(AbstractBaseUser):

    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    #USERNAME_FIELD = 'email' - set this to whatever name you want the user to be able to login with
    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = [] - list of fields that you want to be required.
    #Note: The field name as USERNAME_FIELD must not be name in REQUIRED_FIELDS
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    #This tells the class where the account manager is
    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
