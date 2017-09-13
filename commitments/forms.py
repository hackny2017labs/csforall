from django import forms
from .models import Commitment, Organization

class CommitmentForm(forms.ModelForm):

    class Meta:
        model = Commitment
        fields = ('title', 'description', 'end_date', 'goal_description', 'goal_target',
        		   'contact_name', 'contact_email', 'organizations')

    def __init__(self, *args, **kwargs):
    	super(CommitmentForm, self).__init__(*args, **kwargs)
        self.fields["organizations"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["organizations"].help_text = ""
        self.fields["organizations"].queryset = Organization.objects.all()

class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ('name', 'description')