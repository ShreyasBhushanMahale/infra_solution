from django.shortcuts import redirect, render

from solutions.forms import MaterialForm
from .models import Material, Project, MaintenanceOption


def material_list(request):
    materials = Material.objects.all()
    return render(request, "solutions/material_list.html", {"materials": materials})


def maintenance_options(request, project_id):
    project = Project.objects.get(id=project_id)
    options = MaintenanceOption.objects.filter(project=project)
    return render(
        request,
        "solutions/maintenance_options.html",
        {"project": project, "options": options},
    )


def add_material(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("material_list")
    else:
        form = MaterialForm()
    return render(request, "solutions/add_material.html", {"form": form})
