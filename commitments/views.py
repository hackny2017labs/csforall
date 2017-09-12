# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def commitment_list(request):
    return render(request, 'commitments/commitment_list.html', {})
