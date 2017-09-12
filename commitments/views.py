# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Commitment
from .forms import CommitmentForm

def commitment_list(request):
	commitments = Commitment.objects.filter(create_date__lte=timezone.now()).order_by('create_date')
	return render(request, 'commitments/commitment_list.html', {'commitments': commitments})

def commitment_new(request):
    if request.method == "POST": 
        form = CommitmentForm(request.POST)
        if form.is_valid():
            commitment = form.save(commit=False)
            commitment.create_date = timezone.now()
            commitment.save()
    else:
        form = CommitmentForm()
    return render(request, 'commitments/commitment_new.html', {'form': form})
