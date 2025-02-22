from django.db import models
# Create your models here.
class Infrastructure(models.Model):
  PROJECT_CHOICES = [
    ('building', 'Building'),
    ('road', 'Road'),
    ('bridge', 'Bridge'),
    ('dam', 'Dam'),
    ('tunnel', 'Tunnel'),
  ]

  project_type = models.CharField(max_length=50, choices=PROJECT_CHOICES)
  location = models.CharField(max_length=250)
  budget = models.FloatField()
  materials = models.TextField()
  issues = models.TextField(blank=True)  # A blank field is accepted here.

  def __str__(self):
    return f"{self.project_type} at {self.location}"
