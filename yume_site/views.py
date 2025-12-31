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


def faqs(request):
    return render(request, "faqs.html")

def blog(request):
    return render(request, "blog.html")

def excel_blog(request):
    return render(request, "excel_blog.html")

def sql_blog(request):
    return render(request, "sql_blog.html")

def python_blog(request):
    return render(request, "python_blog.html")

def data_visualization_blog(request):
    return render(request, "data_visualization_blog.html")

def azure_fundamentals_blog(request):
    return render(request, "azure_fundamentals_blog.html")

def ai_azure_blog(request):
    return render(request, "ai_azure_blog.html")

def power_platform_blog(request):
    return render(request, "power_platform_blog.html")

def security_blog(request):
    return render(request, "security_blog.html")

def soft_skills_blog(request):
    return render(request, "soft_skills_blog.html")





def privacy_policy(request):
    return render(request, "privacy_policy.html")

def terms_and_conditions(request):
    return render(request, "terms_and_conditions.html")


def enrollment_form(request):
    return render(request, "enrollment_form.html")

def enquire_now(request):
    return render(request, "enquire_now.html")




from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_page(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        return redirect('contact')  # Prevent duplicate submission

    return render(request, "contact.html")
