from django.urls import path
from . import views
from .views import courses_page, course_detail

from .views import projects_page


urlpatterns = [
    path("", views.home_page, name="home"),
    path("about/", views.about_page, name="about"),
    path("courses/", views.courses_page, name="courses"),
    
    path('courses/<str:course_url>/', course_detail, name='course_detail'),



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
    
    path('projects/aspire_project/', views.aspire_project, name='aspire_project'),
    path('projects/kjk_project/', views.kjk_project, name='kjk_project'),
    path('projects/naan-mudhalvan_project/', views.naan_mudhalvan_project, name='naan_mudhalvan_project'),
    path('projects/bridgetech_project/', views.bridgetech_project, name='bridgetech_project'),
    
    
    
    #   path("projects/", views.projects_page, name="projects"),
    # path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    
    # # Keep old URLs for backward compatibility (redirect to new dynamic URLs)
    # path('projects/aspire_project/', views.aspire_project_redirect, name='aspire_project'),
    # path('projects/kjk_project/', views.kjk_project_redirect, name='kjk_project'),
    # path('projects/naan-mudhalvan_project/', views.naan_mudhalvan_redirect, name='naan_mudhalvan_project'),
    # path('projects/bridgetech_project/', views.bridgetech_project_redirect, name='bridgetech_project'),
    
    
    
    # path("projects/", views.projects_list, name="projects"),
    # path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    
    # path("projects/", projects_page, name="projects"),
    # path("projects/<slug:slug>/", project_detail, name="project_detail"),
    
    path("placements/", views.placements_page, name="placements"),
    path("contact/", views.contact_page, name="contact"),
    
    path("faqs/", views.faqs, name="faqs"),
    
     # Blog URLs
    path("blog/", views.blog, name="blog"),
    path("blog/dynamic/<slug:slug>/", views.dynamic_blog_detail, name="dynamic_blog_detail"),
    
    path("excel_blog/", views.excel_blog, name="excel_blog"),
    path("sql_blog/", views.sql_blog, name="sql_blog"),
    path("python_blog/", views.python_blog, name="python_blog"),
    path("data_visualization_blog/", views.data_visualization_blog, name="data_visualization_blog"),
    path("azure_fundamentals_blog/", views.azure_fundamentals_blog, name="azure_fundamentals_blog"),
    path("ai_azure_blog/", views.ai_azure_blog, name="ai_azure_blog"),
    path("power_platform_blog/", views.power_platform_blog, name="power_platform_blog"),
    path("security_blog/", views.security_blog, name="security_blog"),
    path("soft_skills_blog/", views.soft_skills_blog, name="soft_skills_blog"),
    
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("terms_and_conditions/", views.terms_and_conditions, name="terms_and_conditions"),
    
    path("enrollment_form/", views.enrollment_form, name="enrollment_form"),
    
    path("enquire_now/", views.enquire_now, name="enquire_now"),
    
    
    # path("projects/", views.projects_page, name="projects"),
    # path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    
     # Main projects page with cards
    path('', views.projects_page, name='projects_page'),
    
    # Project detail page
    path('<slug:slug>/', views.project_detail, name='project_detail'),
    
    
 
]
