from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Patient
from .forms import PatientRegistrationForm, PatientSearchForm

@login_required
def patient_list(request):
    form = PatientSearchForm(request.GET)
    patients = Patient.objects.all()
    
    if form.is_valid() and form.cleaned_data['search']:
        search_query = form.cleaned_data['search']
        patients = patients.filter(
            Q(patient_id__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(phone_number__icontains=search_query)
        )
    
    return render(request, 'patients/patient_list.html', {
        'patients': patients,
        'form': form
    })

@login_required
def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request, f'Patient registered successfully. ID: {patient.patient_id}')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientRegistrationForm()
    
    return render(request, 'patients/patient_register.html', {'form': form})

@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient information updated successfully.')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientRegistrationForm(instance=patient)
    
    return render(request, 'patients/patient_edit.html', {'form': form, 'patient': patient})
