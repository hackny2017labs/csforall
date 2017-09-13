# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Commitment, Organization
from .forms import CommitmentForm, OrganizationForm

def commitment_list(request):
	commitments = Commitment.objects.filter(create_date__lte=timezone.now()).order_by('create_date')
	return render(request, 'commitments/commitment_list.html', {
		'commitments': commitments})

def commitment_new(request):
    if request.method == "POST": 
        form = CommitmentForm(request.POST)
        if form.is_valid():
            commitment = form.save(commit=False)
            commitment.create_date = timezone.now()
            commitment.save()
            form.save_m2m()
    else:
        form = CommitmentForm()
    organizations = Organization.objects.filter(create_date__lte=timezone.now()).order_by('create_date')
    return render(request, 'commitments/commitment_new.html', {'form': form, 'organizations': organizations})

def org_new(request):
    if request.method == "POST": 
        form = OrganizationForm(request.POST)
        if form.is_valid():
            org = form.save(commit=False)
            org.create_date = timezone.now()
            org.save()
    else:
        form = OrganizationForm()
    return render(request, 'commitments/org_new.html', {'form': form})
