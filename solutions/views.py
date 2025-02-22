from django.shortcuts import render, redirect
from .models import Infrastructure
from .forms import InfrastructureForm

def generate_suggestions(project_type, location, budget, materials, issues):
    suggestions = []
    if project_type == 'building':
        suggestions.append(f'For construction of a building in {location}, consider using the following: {materials}.')
    elif project_type == 'road':
        suggestions.append(f'A road, if it is built in {location}, should preferably be made of {materials}.')
    elif project_type == 'bridge':
        suggestions.append(f'To build a bridge in {location}, use {materials}, for long term durability.')
    elif project_type == 'dam':
        suggestions.append(f'For a dam in {location}, consider using {materials} for better strength.')
    elif project_type == 'tunnel':
        suggestions.append(f'For drilling a tunnel in {location}, use {materials} for better durability.')
    return suggestions

def project_suggestions(request):
    if request.method == 'POST':
        form = InfrastructureForm(request.POST)
        if form.is_valid():
            project = form.save()
            suggestions = generate_suggestions(project.project_type, project.location, project.budget, project.materials, project.issues)
            return render(request, 'solutions/project_suggestions.html', {'form': form, 'suggestions': suggestions})
    else:
        form = InfrastructureForm()
    return render(request, 'solutions/project_suggestions.html', {'form': form})

