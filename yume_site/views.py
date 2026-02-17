from django.shortcuts import render
from .models import Course

from .models import HeroSlide

def home_page(request):
    hero_slides = HeroSlide.objects.filter(is_active=True).order_by("order")
    return render(request, "home.html", {
        "hero_slides": hero_slides
    })


from django.shortcuts import render
from .models import Advisor, GalleryImage

def about_page(request):
    """About page with dynamic advisors and gallery"""
    
    advisors = Advisor.objects.filter(is_active=True).order_by('display_order', 'created_at')
    gallery_images = GalleryImage.objects.filter(is_active=True).order_by('display_order', 'created_at')
    
    context = {
        "advisors": advisors,
        "gallery_images": gallery_images,
    }
    return render(request, "about.html", context)





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



# def projects_page(request):
#     return render(request, "projects.html")


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

# def contact_page(request):
#     return render(request, "contact.html")




# from django.shortcuts import render
# from .models import PlacementsSection

# def placements_page(request):
#     """Show placements page with dynamic content"""
    
#     # Get active placements sections ordered by display order
#     placements_sections = PlacementsSection.objects.filter(is_active=True).order_by('display_order').first()
    
#     # Get company logos for the first section
#     company_logos = None
#     many_more_section = None
   
    
#     if placements_sections:
#         company_logos = placements_sections.company_logos.filter(is_active=True).order_by('display_order')
#         many_more_section = placements_sections.many_more_section.filter(is_active=True).first()
        
       
    
#     return render(request, "placements.html", {
#         "placements_section": placements_sections,
#         "company_logos": company_logos,
#         "many_more_section": many_more_section,
#     })
    

from django.shortcuts import render
from .models import PlacementsSection, InternshipSection


def placements_page(request):
    placements_section = (
        PlacementsSection.objects
        .filter(is_active=True)
        .order_by('display_order')
        .first()
    )

    company_logos = []
    many_more_section = None

    if placements_section:
        company_logos = placements_section.company_logos.filter(is_active=True)
        many_more_section = placements_section.many_more_section.filter(is_active=True).first()

    internship_section = (
        InternshipSection.objects
        .filter(is_active=True)
        .order_by('display_order')
        .first()
    )

    internship_benefits = internship_section.benefits.all() if internship_section else None

    return render(request, "placements.html", {
        "placements_section": placements_section,
        "company_logos": company_logos,          # ✅ FIX
        "many_more_section": many_more_section,  # ✅ FIX
        "internship_section": internship_section,
        "internship_benefits": internship_benefits,
    })



def courses_page(request):
    courses = Course.objects.filter(is_active=True).order_by('order')
    return render(request, 'courses.html', {'courses': courses})



def faqs(request):
    return render(request, "faqs.html")


# Add these functions to your existing yume_site/views.py

from .models import DynamicBlog
from django.shortcuts import get_object_or_404

def blog(request):
    """Show all blogs (static + dynamic)"""
    # Get all published dynamic blogs
    dynamic_blogs = DynamicBlog.objects.filter(is_published=True).order_by('display_order', '-publish_date')
    
    return render(request, "blog.html", {
        "dynamic_blogs": dynamic_blogs
    })


# def dynamic_blog_detail(request, slug):
#     """Show dynamic blog detail page"""
#     blog_post = get_object_or_404(DynamicBlog, slug=slug, is_published=True)
    
#     # Get related blogs (same category)
#     related_blogs = DynamicBlog.objects.filter(
#         category=blog_post.category,
#         is_published=True
#     ).exclude(id=blog_post.id).order_by('-publish_date')[:3]
    
#     return render(request, "blog_detail.html", {
#         "blog": blog_post,
#         "related_blogs": related_blogs
#     })
    
def dynamic_blog_detail(request, slug):
    """Show dynamic blog detail page"""
    blog_post = get_object_or_404(DynamicBlog, slug=slug, is_published=True)
    
    # Get related blogs (same category)
    related_blogs = DynamicBlog.objects.filter(
        category=blog_post.category,
        is_published=True
    ).exclude(id=blog_post.id).order_by('-publish_date')[:3]
    
    # Get previous blog
    previous_blog = DynamicBlog.objects.filter(
        publish_date__lt=blog_post.publish_date,
        is_published=True
    ).order_by('-publish_date').first()
    
    # Get next blog
    next_blog = DynamicBlog.objects.filter(
        publish_date__gt=blog_post.publish_date,
        is_published=True
    ).order_by('publish_date').first()
    
    return render(request, "blog_detail.html", {
        "blog": blog_post,
        "related_blogs": related_blogs,
        "previous_blog": previous_blog,
        "next_blog": next_blog
    })



# Keep all your existing static blog views (they remain unchanged)
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



# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import ContactMessage

# def contact_page(request):

#     if request.method == "POST":
#         try:
#             ContactMessage.objects.create(
#                 first_name=request.POST.get('first_name'),
#                 last_name=request.POST.get('last_name'),
#                 phone=request.POST.get('phone'),
#                 email=request.POST.get('email'),
#                 message=request.POST.get('message')
#             )

#             return JsonResponse({
#                 "status": "success",
#                 "message": "Thank you! Your message has been sent successfully."
#             })

#         except Exception:
#             return JsonResponse({
#                 "status": "error",
#                 "message": "Something went wrong. Please try again."
#             })

#     return render(request, "contact.html")

from django.shortcuts import render
from django.http import JsonResponse
from .models import ContactMessage, ContactInformation


def contact_page(request):

    contact_info = ContactInformation.objects.first()

    if request.method == "POST":
        try:
            ContactMessage.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                phone=request.POST.get('phone'),
                email=request.POST.get('email'),
                message=request.POST.get('message')
            )

            return JsonResponse({
                "status": "success",
                "message": "Thank you! Your message has been sent successfully."
            })

        except Exception:
            return JsonResponse({
                "status": "error",
                "message": "Something went wrong. Please try again."
            })

    return render(request, "contact.html", {
        "contact_info": contact_info
    })




from django.shortcuts import render
from django.http import JsonResponse
from .models import Enrollment

def enrollment_form(request):

    # 👉 POST: Save data (AJAX)
    if request.method == "POST":
        try:
            Enrollment.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                mobile=request.POST.get('mobile'),
                education=request.POST.get('education'),
                course=request.POST.get('course'),
            )
            return JsonResponse({
                'status': 'success',
                'message': 'Enrollment completed successfully!'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'Something went wrong. Please try again.'
            })

    # 👉 GET: Show enrollment page
    return render(request, "enrollment_form.html")




from django.shortcuts import render
from django.http import JsonResponse
from .models import Enquiry

def enquire_now(request):

    if request.method == "POST":
        try:
            Enquiry.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                mobile=request.POST.get('mobile'),
                message=request.POST.get('message'),
            )

            return JsonResponse({
                "status": "success",
                "message": "Thank you! Your enquiry has been submitted successfully."
            })

        except Exception:
            return JsonResponse({
                "status": "error",
                "message": "Something went wrong. Please try again."
            })

    return render(request, "enquire_now.html")



    



from django.shortcuts import render, get_object_or_404
from .models import Course

def course_detail(request, course_url):
    course = get_object_or_404(
        Course,
        course_url=course_url,
        is_active=True
    )

    curriculum_months = course.curriculum_months.filter(
        is_active=True
    ).prefetch_related(
        "sections__topics"
    )

    return render(
        request,
        "course_detail.html",
        {
            "course": course,
            "curriculum_months": curriculum_months,
        }
    )



from django.shortcuts import render, get_object_or_404
from .models import ProjectCard


def projects_page(request):
    """Show all active project cards"""
    project_cards = ProjectCard.objects.filter(is_active=True).order_by('display_order')
    
    return render(request, "projects.html", {
        "project_cards": project_cards
    })


def project_detail(request, slug):
    """Show project detail page"""
    project_card = get_object_or_404(ProjectCard, slug=slug, is_active=True)
    
    # Get detail page if it exists
    detail_page = None
    if hasattr(project_card, 'detail_page'):
        detail_page = project_card.detail_page
    
    return render(request, "project_detail.html", {
        "project_card": project_card,
        "detail_page": detail_page
    })