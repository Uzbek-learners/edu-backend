from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.core.models import BaseModel
from apps.users.queryset import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=50)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(5), MaxValueValidator(116)]
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_mentor = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def full_name(self):
        first_name = str(self.first_name) if self.first_name else ""
        last_name = str(self.last_name) if self.last_name else ""
        full_name = " ".join([first_name, last_name])
        return full_name.strip()

    class Meta:
        db_table = "users"
