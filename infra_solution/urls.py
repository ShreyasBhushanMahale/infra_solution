from django.urls import path
from solutions import views

urlpatterns = [
    path("create-project/", views.project_create, name="project_create"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path("create-maintenance/", views.maintenance_create, name="maintenance_create"),
    path("maintenance/<int:pk>/", views.maintenance_detail, name="maintenance_detail"),
]
