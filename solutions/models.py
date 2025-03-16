# The models:
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ("Building", "Building"),
        ("Bridge", "Bridge"),
        ("Tunnel", "Tunnel"),
        ("Dam", "Dam"),
        ("Road", "Road"),
    ]

    name = models.CharField(max_length=200)
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    region = models.CharField(max_length=200)
    materials_suggested = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Maintenance(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    defect_details = models.TextField()
    next_maintenance_date = models.DateField()
    action_suggested = models.TextField()

    def __str__(self):
        return f"Maintenance for {self.project.name}"
