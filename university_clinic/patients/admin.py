from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'first_name', 'last_name', 'phone_number', 'registration_date')
    list_filter = ('registration_date', 'is_active', 'gender')
    search_fields = ('patient_id', 'first_name', 'last_name', 'phone_number')
    readonly_fields = ('patient_id', 'registration_date', 'last_updated')
    fieldsets = (
        ('Personal Information', {
            'fields': ('patient_id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'blood_group')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'email', 'address')
        }),
        ('Medical Information', {
            'fields': ('allergies', 'medical_conditions', 'current_medications')
        }),
        ('System Information', {
            'fields': ('registration_date', 'last_updated', 'is_active')
        }),
    )
