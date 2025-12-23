from django.shortcuts import render

def home_page(request):
    return render(request, "home.html")

def about_page(request):
    return render(request, "about.html")



def courses_page(request):
    return render(request, "courses.html")

def excel_course(request):
    return render(request, "courses/excel_data_analysis.html")

def sql_course(request):
    return render(request, "courses/sql_data_analysis.html")

def python_course(request):
    return render(request, "courses/python_development.html")

def visualization_course(request):
    return render(request, "courses/data_visualization.html")

def azure_course(request):
    return render(request, "courses/azure_fundamentals.html")

def azure_ai_course(request):
    return render(request, "courses/azure_ai_fundamentals.html")

def power_platform_course(request):
    return render(request, "courses/power_platform.html")

def security_course(request):
    return render(request, "courses/security_compliance.html")

def professional_dev_course(request):
    return render(request, "courses/professional_development.html")



def projects_page(request):
    return render(request, "projects.html")


def aspire_project(request):
    return render(request, 'aspire_project.html')

def kjk_project(request):
    return render(request, 'kjk_project.html')

def naan_mudhalvan_project(request):
    return render(request, 'naan_mudhalvan_project.html')

def bridgetech_project(request):
    return render(request, 'bridgetech_project.html')



def placements_page(request):
    return render(request, "placements.html")

def contact_page(request):
    return render(request, "contact.html")
