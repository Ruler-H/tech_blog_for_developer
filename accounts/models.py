from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        email = self.normalize_email(email)
        user = self.model(
            username = username,
            email = email,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return super()._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    nickname = models.CharField(max_length=50, unique=True, null=False)
    phone = models.CharField(max_length=50, unique=True, blank=True, null=True)
    development_field = models.CharField(max_length=50, null=False)
    profile_image = models.ImageField(upload_to='accounts/%Y/%m/%d/', blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True, null=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nickname']

    objects = CustomUserManager()

    def __str__(self):
        return self.nickname
    
    def get_short_name(self):
        return self.nickname
    
    def get_full_name(self):
        return self.nickname
    
    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
