from django.shortcuts import render
from .forms import InfrastructureForm, IssuesForm
from .models import Infrastructure

def project_suggestions(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'infrastructure_form':
            form = InfrastructureForm(request.POST)
            if form.is_valid():
                project = form.save()
                suggestions = generate_suggestions(project.project_type, project.location, project.budget, project.materials, project.issues)
                return render(request, 'solutions/project_suggestions.html', {'form': form, 'suggestions': suggestions, 'issues_form': IssuesForm()})
        elif form_type == 'issues_form':
            issues_form = IssuesForm(request.POST)
            if issues_form.is_valid():
                issues = issues_form.cleaned_data['issues']
                # Process issues and generate solutions
                solutions = generate_solutions_for_issues(issues)
                return render(request, 'solutions/project_suggestions.html', {'form': InfrastructureForm(), 'issues_form': issues_form, 'issues': issues, 'solutions': solutions})
    else:
        form = InfrastructureForm()
        issues_form = IssuesForm()

    return render(request, 'solutions/project_suggestions.html', {'form': form, 'issues_form': issues_form})

def project_issues(request):
    if request.method == 'GET':
        # Retrieve the existing infrastructure projects from the database
        projects = Infrastructure.objects.all()
        # Process the projects and generate solutions based on their issues
        issues = []
        solutions = []
        for project in projects:
            issues.append({'id': project.id, 'issues': project.issues})
            if project.issues == 'leakage':
                solutions.append(f'To address leakage issue in project {project.id}, consider using waterproof materials.')
            elif project.issues == 'structural damage':
                solutions.append(f'To address structural damage issue in project {project.id}, consider conducting a thorough inspection and repair. If that does not work, consider rebuilding the structure.')
            elif project.issues == 'corrosion':
                solutions.append(f'To address corrosion issue in project {project.id}, consider using anti-corrosive coatings and materials.')
            elif project.issues == 'poor water flow':
                solutions.append(f'To address poor water flow issue in project {project.id}, consider redesigning the water flow system and ensuring proper maintenance.')
            elif project.issues == 'cracks':
                solutions.append(f'To address cracks issue in project {project.id}, consider applying crackseal, conducting structural analysis, and carrying out repair work.')
            elif project.issues == 'erosion':
                solutions.append(f'To address erosion issue in project {project.id}, consider using erosion control measures such as retaining walls or vegetation.')

        return render(request, 'solutions/project_issues.html', {'projects': projects, 'issues': issues, 'solutions': solutions})
    else:
        return render(request, 'solutions/project_issues.html', {})