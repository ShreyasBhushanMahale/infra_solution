from django import forms
from .models import Project, Maintenance


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "project_type", "budget", "region"]


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ["project", "defect_details", "next_maintenance_date"]
