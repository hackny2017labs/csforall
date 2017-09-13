from django import forms
from .models import Commitment, Organization

class CommitmentForm(forms.ModelForm):

    class Meta:
        model = Commitment
        fields = ('title', 'description', 'end_date', 'goal_description', 'goal_target',
        		   'contact_name', 'contact_email')

class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ('name', 'description')