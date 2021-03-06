from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from .managers import MyUserManager
from django.core.mail import send_mail
import uuid

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
                        verbose_name='email address',
                        max_length=255,
                        unique=True,
                    )
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=True)
    user_hash = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
        


