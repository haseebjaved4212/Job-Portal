from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('seeker', 'Job Seeker'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='seeker')

    def __str__(self):
        return self.username
    def is_employer(self):
        return self.role == 'employer'
    def is_seeker(self):
        return self.role == 'seeker'
    def is_admin(self):
        return self.role == 'admin'