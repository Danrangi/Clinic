from django.db import models
from django.core.validators import RegexValidator

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    # Personal Information
    patient_id = models.CharField(max_length=10, unique=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True, null=True)
    
    # Contact Information
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    
    # Medical Information
    allergies = models.TextField(blank=True)
    medical_conditions = models.TextField(blank=True)
    current_medications = models.TextField(blank=True)
    
    # System Information
    registration_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.patient_id:
            # Generate patient ID (You can customize this format)
            last_patient = Patient.objects.order_by('-id').first()
            if last_patient:
                last_id = int(last_patient.patient_id[3:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.patient_id = f'PAT{new_id:06d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient_id} - {self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-registration_date']
