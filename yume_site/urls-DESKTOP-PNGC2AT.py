from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about/", views.about_page, name="about"),
    path("courses/", views.courses_page, name="courses"),

    path("courses/excel-data-analysis/", views.excel_course, name="excel"),
    path("courses/sql-data-analysis/", views.sql_course, name="sql"),
    path("courses/python-development/", views.python_course, name="python"),
    path("courses/data-visualization/", views.visualization_course, name="visualization"),
    path("courses/azure-fundamentals/", views.azure_course, name="azure"),
    path("courses/azure-ai-fundamentals/", views.azure_ai_course, name="azure_ai"),
    path("courses/power-platform/", views.power_platform_course, name="power_platform"),
    path("courses/security-compliance/", views.security_course, name="security"),
    path("courses/professional-development/", views.professional_dev_course, name="professional_dev"),

    path("projects/", views.projects_page, name="projects"),
    path("placements/", views.placements_page, name="placements"),
    path("contact/", views.contact_page, name="contact"),
]
