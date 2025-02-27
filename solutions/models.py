from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    material_type = models.CharField(
        max_length=100,
        choices=[
            ("concrete", "Concrete"),
            ("steel", "Steel"),
            ("wood", "Wood"),
            ("glass", "Glass"),
        ],
    )
    suitable_for = models.TextField(
        help_text="Type of projects this material is suitable for (e.g., bridges, buildings)"
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    project_type = models.CharField(
        max_length=100,
        choices=[
            ("building", "Building"),
            ("bridge", "Bridge"),
            ("road", "Road"),
            ("tunnel", "Tunnel"),
            ("dam", "Dam"),
        ],
    )
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class MaintenanceOption(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=50, help_text="E.g., monthly, yearly")

    def __str__(self):
        return f"Maintenance for {self.project.name}"
