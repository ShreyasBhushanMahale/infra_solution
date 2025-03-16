from django.shortcuts import render


# Function to suggest materials based on project type
def suggest_materials(project_type):
    material_suggestions = {
        "building": ["Concrete", "Steel", "Glass"],
        "bridge": ["Steel", "Concrete"],
        "road": ["Asphalt", "Concrete"],
        "tunnel": ["Concrete", "Steel"],
        "dam": ["Concrete", "Steel"],
    }
    return material_suggestions.get(project_type, ["General Building Material"])


# Function to suggest maintenance options based on project type
def suggest_maintenance(project_type):
    maintenance_suggestions = {
        "building": ["Annual HVAC check", "Fire safety inspection"],
        "bridge": ["Yearly structural inspection", "Corrosion check"],
        "road": ["Pothole repair", "Resurfacing"],
        "tunnel": ["Structural integrity inspection", "Ventilation system check"],
        "dam": ["Spillway inspection", "Seepage monitoring"],
    }
    return maintenance_suggestions.get(project_type, ["General Maintenance"])


def get_suggestions(request):
    if request.method == "POST":
        project_type = request.POST.get("project_type")
        location = request.POST.get("location")  # Not used yet, but can be later

        # Get suggestions for materials and maintenance
        materials = suggest_materials(project_type)
        maintenance = suggest_maintenance(project_type)

        # Pass the results to the template
        return render(
            request,
            "solutions/suggestions.html",
            {
                "materials": materials,
                "maintenance": maintenance,
                "project_type": project_type,
                "location": location,
            },
        )

    # Render the form page
    return render(request, "solutions/form.html")
