from django import forms
from .models import Infrastructure   # This is the class which we created earlier in models.py file.

class InfrastructureForm(forms.ModelForm):
  class Meta:
    model = Infrastructure
    fields = ['project_type', 'location', 'budget', 'materials', 'issues']
    widgets = {
      'project_type': forms.Select(attrs={'class': 'form-control'}),
      'location': forms.TextInput(attrs={'class': 'form-control'}),
      'budget': forms.NumberInput(attrs={'class': 'form-control'}),
      'materials': forms.Textarea(attrs={'class': 'form-control'}),
      'issues': forms.Textarea(attrs={'class': 'form-control'}),
    }
