from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_user(self, phone, username, email, full_name, password, age, **other_fields):
        if not phone:
            raise ValueError('Enter Phone!')

        email = self.normalize_email(email)
        user = self.model(phone=phone, username=username,  email=email, full_name=full_name, age=age, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, username, email, full_name, password, age, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('is_staff Must Be True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser Must Be True')

        return self.create_user(phone, username, email, full_name, password, age, **other_fields)


class CustomGroup(models.Model):
    pass

class CustomPermission(models.Model):
    pass
class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=70, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    age = models.PositiveSmallIntegerField()
    groups = models.ManyToManyField(CustomGroup, related_name='users')
    user_permissions = models.ManyToManyField(CustomPermission, related_name='users')
    username = models.CharField(max_length=40, unique=True)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ('username', 'email', 'full_name', 'age')

    def __str__(self):
        return f'{self.full_name}-{self.phone}'

class Otp(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='verification_codes')
    verification_code = models.CharField(max_length=4)
    token = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return f'{self.verification_code}-{self.user.username}'
