from django import forms
from .models import Commitment

class CommitmentForm(forms.ModelForm):

    class Meta:
        model = Commitment
        fields = ('title', 'description', 'end_date', 'goal_description', 'goal_target')