from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, MaintenanceForm
from .models import Project, Maintenance


def smart_suggestion_logic(project):
    # Implement suggestions based on project type
    if project.project_type == "Dam":
        return "Use roller-compacted concrete for dam construction."
    elif project.project_type == "Road":
        return "Use asphalt or reinforced concrete depending on traffic load."
    elif project.project_type == "Building":
        return "Use steel and concrete for high-rise buildings."
    elif project.project_type == "Bridge":
        return "Balanced cantilever method for bridge construction."
    elif project.project_type == "Tunnel":
        return "Bored tunnel method recommended for urban areas."
    return "General construction materials recommended."


def maintenance_suggestion_logic(maintenance):
    # Implement suggestions based on defect details
    defect = maintenance.defect_details.lower()
    if "crack" in defect:
        return "Inspect structural integrity and consider repairs."
    elif "leak" in defect:
        return "Check for water damage and promptly seal leaks."
    # Additional conditions can be added here.
    return "Schedule a detailed maintenance inspection."


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.materials_suggested = smart_suggestion_logic(project)
            project.user = request.user  # Assuming the user is logged in
            project.save()
            return redirect("project_detail", pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, "project_form.html", {"form": form})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "project_detail.html", {"project": project})


def maintenance_create(request):
    if request.method == "POST":
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.action_suggested = maintenance_suggestion_logic(maintenance)
            maintenance.save()
            return redirect("maintenance_detail", pk=maintenance.pk)
    else:
        form = MaintenanceForm()
    return render(request, "maintenance_form.html", {"form": form})


def maintenance_detail(request, pk):
    maintenance = get_object_or_404(Maintenance, pk=pk)
    return render(request, "maintenance_detail.html", {"maintenance": maintenance})
