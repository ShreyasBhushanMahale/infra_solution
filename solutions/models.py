from django.db import models

class Infrastructure(models.Model):
    PROJECT_CHOICES = [
        ('building', 'Building'),
        ('road', 'Road'),
        ('bridge', 'Bridge'),
        ('dam', 'Dam'),
        ('tunnel', 'Tunnel'),
    ]

    ISSUE_CHOICES = [
        ('leakage', 'Leakage'),
        ('structural damage', 'Structural Damage'),
        ('corrosion', 'Corrosion'),
        ('poor water flow', 'Poor Water Flow'),
        ('cracks', 'Cracks'),
        ('erosion', 'Erosion'),
    ]

    project_type = models.CharField(max_length=50, choices=PROJECT_CHOICES)
    location = models.CharField(max_length=250)
    budget = models.FloatField()
    materials = models.TextField()
    issues = models.CharField(max_length=50, choices=ISSUE_CHOICES, blank=True)  # Changed to CharField with choices

    def __str__(self):
        return f"{self.project_type} at {self.location}"