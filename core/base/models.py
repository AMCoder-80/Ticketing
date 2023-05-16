from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        create and save a UserObject as a ordinary user
        with the given email and password and extra data. 
        """
        if not email :
            raise ValueError('The Email must be set.')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    

    def create_superuser(self, email, password, **extra_fields):
        """
        create and save a User object as a superuser 
        with given email and password and extra data.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):

    first_name = models.CharField(max_length=30, verbose_name='نام')
    last_name = models.CharField(max_length=30, verbose_name='نام خانوادگی')
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=11, verbose_name='شماره موبایل')

    username = None
    helpical_id = models.IntegerField(null=True, blank=True)
    helpical_password = models.CharField(max_length=255, null=True, blank=True)

    customer_created = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    def __str__(self):
        return self.email
