from django import forms
from .models import Material, Project, MaintenanceOption

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'description', 'material_type', 'suitable_for']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'project_type', 'location', 'description']

class MaintenanceOptionForm(forms.ModelForm):
    class Meta:
        model = MaintenanceOption
        fields = ['project', 'description', 'cost', 'frequency']