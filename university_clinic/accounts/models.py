from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    FRONT_DESK = 'front_desk'
    DOCTOR = 'doctor'
    PHARMACIST = 'pharmacist'
    ADMIN = 'admin'
    AUDITOR = 'auditor'

    ROLE_CHOICES = [
        (FRONT_DESK, 'Front Desk'),
        (DOCTOR, 'Doctor'),
        (PHARMACIST, 'Pharmacist'),
        (ADMIN, 'Admin'),
        (AUDITOR, 'Auditor'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"
