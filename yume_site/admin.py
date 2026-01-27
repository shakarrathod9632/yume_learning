from django.contrib import admin
from .models import (
    ContactMessage,
    Enrollment,
    Enquiry,
    Course,
    CourseHighlight,
    CurriculumMonth,
    CurriculumSection,
    CurriculumTopic,
    CourseLearningOutcome,
    CourseTool,
    CourseCertificationPoint,
    CourseFAQ,
)

# ==========================
# Contact / Enrollment / Enquiry
# ==========================

from django.contrib import admin
from .models import ContactMessage, ContactInformation


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "submitted_at")
    search_fields = ("first_name", "last_name", "email", "phone")
    list_filter = ("submitted_at",)


@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Contact Information", {
            "fields": ("address", "phone", "email")
        }),
    )


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name", "last_name", "email", "mobile",
        "education", "course", "created_at"
    )
    search_fields = ("first_name", "last_name", "email", "mobile")
    list_filter = ("education", "course", "created_at")


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "mobile", "created_at")
    search_fields = ("first_name", "last_name", "email", "mobile")
    list_filter = ("created_at",)


    


from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import (
    Course, CourseHighlight, CurriculumMonth, CurriculumSection, 
    CurriculumTopic, CourseLearningOutcome, CourseTool,
    CourseCertificationPoint, CourseFAQ, CourseCareerOpportunity
)


# =========================
# COURSE HIGHLIGHTS INLINE
# =========================
class CourseHighlightInline(admin.StackedInline):
    model = CourseHighlight
    extra = 0
    max_num = 4
    ordering = ("order",)
    fields = ("icon_class", "title", "description", "order", "is_active")
    verbose_name_plural = "⭐ Course Highlights (Top Section)"


# =========================
# CURRICULUM MONTH INLINE
# =========================
class CurriculumMonthInline(admin.StackedInline):
    model = CurriculumMonth
    extra = 0
    ordering = ("order",)
    fields = ("title", "subtitle", "meta_info", "badge_color", "order", "is_active")
    verbose_name_plural = "📅 Curriculum Months"


# =========================
# CURRICULUM SECTION INLINE
# =========================
class CurriculumSectionInline(admin.StackedInline):
    model = CurriculumSection
    extra = 0
    ordering = ("order",)
    fields = ("month", "title", "order")
    verbose_name_plural = "📋 Curriculum Sections (Weeks/Units)"
    
    formfield_overrides = {
        models.CharField: {
            "widget": TextInput(attrs={
                "style": "width: 100%;"
            })
        }
    }


# =========================
# CURRICULUM TOPIC INLINE
# =========================
class CurriculumTopicInline(admin.StackedInline):
    model = CurriculumTopic
    extra = 0
    ordering = ("order",)
    fields = ("section", "title", "order")
    verbose_name_plural = "📝 Curriculum Topics (Lessons)"
    
    formfield_overrides = {
        models.CharField: {
            "widget": TextInput(attrs={
                "style": "width: 100%;"
            })
        }
    }


# =========================
# LEARNING OUTCOMES INLINE
# =========================
class CourseLearningOutcomeInline(admin.StackedInline):
    model = CourseLearningOutcome
    extra = 0
    ordering = ("order",)

    fieldsets = (
        ("Learning Outcomes & Career Benefits", {
            "fields": (
                "title",
                "description",
                ("color", "order"),
            ),
            "description": "What students will gain after completing this course",
        }),
    )

    formfield_overrides = {
        models.TextField: {
            "widget": Textarea(attrs={
                "rows": 4,
                "style": "width: 100%; resize: vertical;",
            })
        }
    }

    verbose_name = "Learning Outcome"
    verbose_name_plural = "📘 Learning Outcomes & Career Benefits"


# =========================
# TOOLS & TECHNOLOGIES INLINE
# =========================
class CourseToolInline(admin.StackedInline):
    model = CourseTool
    extra = 0
    ordering = ("order",)

    fieldsets = (
        ("Tools & Technologies", {
            "fields": (
                "name",
                "description",
                ("color", "order"),
            ),
            "description": "Tools used in this course",
        }),
    )

    formfield_overrides = {
        models.TextField: {
            "widget": Textarea(attrs={
                "rows": 3,
                "style": "width: 100%; resize: vertical;",
            })
        }
    }

    verbose_name = "Tool / Technology"
    verbose_name_plural = "🛠 Tools & Technologies"


# =========================
# CERTIFICATION INLINE
# =========================
class CourseCertificationPointInline(admin.StackedInline):
    model = CourseCertificationPoint
    extra = 0
    ordering = ("order",)
    fields = ("text", "order")
    verbose_name_plural = "🏆 Certification & Placement Support"

    formfield_overrides = {
        models.CharField: {
            "widget": TextInput(attrs={
                "style": "width: 100%;"
            })
        }
    }


# =========================
# FAQ INLINE
# =========================
class CourseFAQInline(admin.StackedInline):
    model = CourseFAQ
    extra = 0
    ordering = ("order",)
    fields = ("question", "answer", "order")

    formfield_overrides = {
        models.TextField: {
            "widget": Textarea(attrs={
                "rows": 3,
                "style": "width:100%; resize:vertical;"
            })
        }
    }

    verbose_name_plural = "❓ Frequently Asked Questions"


# =========================
# CAREER OPPORTUNITIES INLINE
# =========================
class CourseCareerOpportunityInline(admin.StackedInline):
    model = CourseCareerOpportunity
    extra = 0
    ordering = ("order",)

    fields = (
        "title",
        "description",
        "tag",
        "icon_type",
        "order",
    )

    verbose_name_plural = "💼 Career Opportunities"

    formfield_overrides = {
        models.CharField: {
            "widget": TextInput(attrs={
                "style": "width: 100%;"
            })
        },
        models.TextField: {
            "widget": Textarea(attrs={
                "rows": 2,
                "style": "width: 100%; resize: vertical;"
            })
        },
    }


# =========================
# COURSE ADMIN (MAIN)
# =========================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "course_url", "is_active", "order")
    list_editable = ("is_active", "order")
    search_fields = ("title", "course_url")
    ordering = ("order",)

    fieldsets = (
        ("📋 Basic Information", {
            "fields": (
                "title",
                "card_description",
                "image",
            ),
            "description": "Course card shown on listing page"
        }),
        
        ("🎯 Course Details", {
            "fields": (
                "subtitle",
                "overview",
            ),
            "description": "Main description for course detail page"
        }),
        
        ("📊 Course Specifications", {
            "fields": (
                "duration",
                "total_hours",
                "level",
                "format",
            ),
            "description": "Technical specifications"
        }),
        
        ("📞 Contact Information", {
            "fields": (
                "whatsapp_number",
                "contact_number",
            ),
            "description": "For enrollment and queries"
        }),
        
        ("⚙️ Settings", {
            "fields": (
                "course_url",
                "order",
                "is_active",
            ),
            "description": "Technical settings"
        }),
    )

    inlines = [
        CourseHighlightInline,           # 1. Highlights (top section)
        CurriculumMonthInline,           # 2. Months (Month 1, Month 2)
        CurriculumSectionInline,         # 3. Sections (Week 1-2, Week 3-4)
        CurriculumTopicInline,           # 4. Topics (specific lessons)
        CourseLearningOutcomeInline,     # 5. Learning Outcomes
        CourseToolInline,                # 6. Tools & Technologies
        CourseCertificationPointInline,  # 7. Certification
        CourseFAQInline,                 # 8. FAQs
        CourseCareerOpportunityInline,   # 9. Career Opportunities
    ]

    formfield_overrides = {
        models.CharField: {
            "widget": TextInput(attrs={
                "style": "width: 100%;"
            })
        },
        models.TextField: {
            "widget": Textarea(attrs={
                "rows": 4,
                "style": "width: 100%; resize: vertical;"
            })
        },
    }

    class Media:
        css = {
            'all': ('admin/css/courses.css',)
        }




ds = ['project_card']


from django.contrib import admin
from django.utils.html import format_html
from .models import ProjectCard, ProjectDetail


class ProjectDetailInline(admin.StackedInline):
    """Inline editor for detail page BELOW the card"""
    model = ProjectDetail
    can_delete = False
    verbose_name_plural = "Project Detail Page"
    verbose_name = "Detail Page Content"
    
    # User-friendly field grouping
    fieldsets = (
        ('📋 Header & Badges', {
            'fields': ('badge_text', 'launch_date_badge'),
            'description': 'Customize the header badges'
        }),
        
        ('🖼️ Hero Image', {
            'fields': ('hero_image',),
            'description': 'Large image for detail page (optional)'
        }),
        
        ('📊 Key Metrics', {
            'fields': ('duration_hours', 'student_count', 'location'),
            'description': 'Statistics shown in metrics section'
        }),
        
        ('🎯 Target Audience', {
            'fields': ('target_audience',),
            'description': 'Who is this program for?'
        }),
        
        ('🤝 Partners Section', {
            'fields': ('show_partners',),
            'description': 'Show or hide partners section'
        }),
        
        ('👥 Partner 1', {
            'fields': ('partner_1_name', 'partner_1_type', 'partner_1_icon', 'partner_1_color'),
            'description': 'First partner details'
        }),
        
        ('👥 Partner 2', {
            'fields': ('partner_2_name', 'partner_2_type', 'partner_2_icon', 'partner_2_color'),
            'description': 'Second partner details'
        }),
        
        ('👥 Partner 3', {
            'fields': ('partner_3_name', 'partner_3_type', 'partner_3_icon', 'partner_3_color'),
            'description': 'Third partner details'
        }),
        
        ('📝 Detailed Content', {
            'fields': ('detailed_content',),
            'description': 'Full project description for detail page'
        }),
        
        ('📋 Program Overview Section (Dynamic)', {
            'fields': ('show_program_overview',),
            'description': 'Toggle program overview section'
        }),
        
        ('🎯 Program Overview Content', {
            'fields': (
                'program_overview_title',
                'program_objective',
                'implementing_partner_name',
                'partner_2_name_overview',
                'partner_3_name_overview',
            ),
            'description': 'Content for program overview section'
        }),
        
        ('📚 Learning Approach Box', {
            'fields': (
                'learning_approach_title',
                'learning_approach_main',
                'learning_approach_sub',
                'learning_approach_icon',
            ),
            'description': 'Learning approach box details'
        }),
        
                ('🎯 Program Components Section', {
            'fields': ('show_program_components',),
            'description': 'Toggle program components section'
        }),
        
        ('📋 Component 1 - Technical Skills', {
            'fields': (
                'component_1_title',
                'component_1_subtitle',
                'component_1_icon',
                'component_1_color',
                'component_1_items',
            ),
            'description': 'First program component details'
        }),
        
        ('📋 Component 2 - Hands-on Projects', {
            'fields': (
                'component_2_title',
                'component_2_subtitle',
                'component_2_icon',
                'component_2_color',
                'component_2_items',
            ),
            'description': 'Second program component details'
        }),
        
        ('📋 Component 3 - Career Development', {
            'fields': (
                'component_3_title',
                'component_3_subtitle',
                'component_3_icon',
                'component_3_color',
                'component_3_items',
            ),
            'description': 'Third program component details'
        }),
        
                ('🎯 Role & Impact Section', {
            'fields': ('show_role_impact',),
            'description': 'Toggle role and impact section'
        }),
        
        ('👥 Implementing Partner Role', {
            'fields': (
                'role_title',
                'role_description',
            ),
            'description': 'Main role description'
        }),
        
        ('🔧 Role Item 1', {
            'fields': (
                'role_item_1_title',
                'role_item_1_subtitle',
                'role_item_1_icon',
                'role_item_1_color',
            ),
            'description': 'First role responsibility'
        }),
        
        ('🔧 Role Item 2', {
            'fields': (
                'role_item_2_title',
                'role_item_2_subtitle',
                'role_item_2_icon',
                'role_item_2_color',
            ),
            'description': 'Second role responsibility'
        }),
        
        ('🔧 Role Item 3', {
            'fields': (
                'role_item_3_title',
                'role_item_3_subtitle',
                'role_item_3_icon',
                'role_item_3_color',
            ),
            'description': 'Third role responsibility'
        }),
        
        ('🔧 Role Item 4', {
            'fields': (
                'role_item_4_title',
                'role_item_4_subtitle',
                'role_item_4_icon',
                'role_item_4_color',
            ),
            'description': 'Fourth role responsibility'
        }),
        
        ('📊 Program Impact', {
            'fields': (
                'impact_title',
                'impact_main_number',
                'impact_main_text',
                'impact_metric_1_number',
                'impact_metric_1_text',
                'impact_metric_2_number',
                'impact_metric_2_text',
            ),
            'description': 'Impact statistics'
        }),
        
        ('📈 Outcome Metrics', {
            'fields': (
                'outcome_1_label',
                'outcome_1_value',
                'outcome_1_color',
                'outcome_2_label',
                'outcome_2_value',
                'outcome_2_color',
                'outcome_3_label',
                'outcome_3_value',
                'outcome_3_color',
            ),
            'description': 'Outcome progress bars'
        }),
        
        
            ('🏆 Certification & Support Section', {
            'fields': ('show_certification_support',),
            'description': 'Toggle certification and support section'
        }),
        
        ('📜 Certification Card', {
            'fields': (
                'certification_title',
                'certification_subtitle',
                'certification_description',
                'certification_icon',
                'certification_color',
            ),
            'description': 'Certification card details'
        }),
        
        ('✅ Certification Features', {
            'fields': (
                ('cert_feature_1_text', 'cert_feature_1_icon', 'cert_feature_1_color'),
                ('cert_feature_2_text', 'cert_feature_2_icon', 'cert_feature_2_color'),
                ('cert_feature_3_text', 'cert_feature_3_icon', 'cert_feature_3_color'),
                ('cert_feature_4_text', 'cert_feature_4_icon', 'cert_feature_4_color'),
            ),
            'description': 'Certification features (4 items)'
        }),
        
        ('💼 Support Card', {
            'fields': (
                'support_title',
                'support_subtitle',
                'support_description',
                'support_icon',
                'support_color',
            ),
            'description': 'Support card details'
        }),
        
        ('✅ Support Features', {
            'fields': (
                ('support_feature_1_text', 'support_feature_1_icon', 'support_feature_1_color'),
                ('support_feature_2_text', 'support_feature_2_icon', 'support_feature_2_color'),
                ('support_feature_3_text', 'support_feature_3_icon', 'support_feature_3_color'),
                ('support_feature_4_text', 'support_feature_4_icon', 'support_feature_4_color'),
            ),
            'description': 'Support features (4 items)'
        }),
        
        
                ('🌱 Sustainable Pathways Section', {
            'fields': ('show_sustainable_pathways',),
            'description': 'Toggle sustainable pathways section'
        }),
        
        ('📋 Main Content', {
            'fields': (
                'pathways_title',
                'pathways_description',
            ),
            'description': 'Main content for sustainable pathways'
        }),
        
        ('🏷️ Partner Badges', {
            'fields': (
                ('partner_badge_1_name', 'partner_badge_1_icon', 'partner_badge_1_color'),
                ('partner_badge_2_name', 'partner_badge_2_icon', 'partner_badge_2_color'),
                ('partner_badge_3_name', 'partner_badge_3_icon', 'partner_badge_3_color'),
            ),
            'description': 'Partner badges (3 badges)'
        }),
        
        ('⭐ Program Highlights', {
            'fields': (
                'highlights_title',
                'highlight_1_text',
                'highlight_1_color',
                'highlight_2_text',
                'highlight_2_color',
                'highlight_3_text',
                'highlight_3_color',
            ),
            'description': 'Program highlights in right column'
        }),
    )
    
    # Help texts for each field
    help_texts = {
        'badge_text': 'e.g., Skill Development Program, Technology Training',
        'launch_date_badge': 'e.g., July 2025 Launch, Ongoing Program',
        'duration_hours': 'e.g., 120 Hours, 50 Hours',
        'student_count': 'Number of students in the program',
        'location': 'e.g., Bengaluru, Karnataka, Pan-India',
        'detailed_content': 'Detailed description of the project',
        'partner_1_icon': 'Select an icon that represents this partner',
        'partner_2_icon': 'Select an icon that represents this partner',
        'partner_3_icon': 'Select an icon that represents this partner',
        
        'program_overview_title': 'Title for program overview section',
        'program_objective': 'Describe the program objective and purpose',
        'implementing_partner_name': 'Main implementing partner name',
        'learning_approach_icon': 'Select icon for learning approach box',
        'components_title': 'Title for program components section',
        
        'component_1_items': 'Enter one item per line (press Enter for new line)',
        'component_2_items': 'Enter one item per line (press Enter for new line)',
        'component_3_items': 'Enter one item per line (press Enter for new line)',
        
        'outcome_1_value': 'Enter percentage value (0-100)',
        'outcome_2_value': 'Enter percentage value (0-100)',
        'outcome_3_value': 'Enter percentage value (0-100)',
    }
    
    
    
    


@admin.register(ProjectCard)
class ProjectCardAdmin(admin.ModelAdmin):
    """Admin for Project Cards"""
    
    # === LIST VIEW ===
    list_display = [
        'project_name', 
        'category', 
        'duration', 
        'is_active',
        'has_detail_page',
        'image_preview'
    ]
    
    list_filter = ['is_active', 'category']
    search_fields = ['project_name', 'tagline']
    list_editable = ['is_active']
    
    # === FORM FIELDSETS ===
    fieldsets = (
        ('📋 Basic Information', {
            'fields': (
                'project_name',
                'tagline',
                'category',
                'duration',
                'thumbnail_image',
                'image_preview',
            ),
            'description': 'Basic details for the project card'
        }),
        
        ('📝 Card Description', {
            'fields': (
                'short_description',
            ),
            'description': 'Brief description for project card'
        }),
        
        ('⚙️ Display Settings', {
            'fields': (
                'display_order',
                'is_active',
            ),
            'description': 'Control how the card appears'
        }),
    )
    
    # === INLINE (Detail page appears BELOW) ===
    inlines = [ProjectDetailInline]
    
    # === READONLY FIELDS ===
    readonly_fields = ['image_preview', 'has_detail_page']
    
    # === CUSTOM METHODS ===
    def image_preview(self, obj):
        if obj.thumbnail_image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px; border-radius: 4px;" />',
                obj.thumbnail_image.url
            )
        return "No image uploaded"
    image_preview.short_description = 'Image Preview'
    
    def has_detail_page(self, obj):
        return hasattr(obj, 'detail_page') and obj.detail_page is not None
    has_detail_page.boolean = True
    has_detail_page.short_description = 'Has Detail Page'






from .models import DynamicBlog
# Update the DynamicBlogAdmin class in your existing admin.py

@admin.register(DynamicBlog)
class BlogAdmin(admin.ModelAdmin):  # Changed class name to BlogAdmin
    """Admin for Blogs"""
    
    # === LIST VIEW ===
    list_display = [
        'title', 
        'category_display', 
        'publish_date', 
        'is_published',
        'featured',
        'image_preview',
        'display_order'
    ]
    
    list_filter = ['is_published', 'featured', 'category', 'publish_date']
    search_fields = ['title', 'excerpt', 'author_name']
    list_editable = ['is_published', 'featured', 'display_order']
    date_hierarchy = 'publish_date'
    
    # === FORM FIELDSETS ===
    fieldsets = (
        ('📋 Basic Information (For Blog Card)', {
            'fields': (
                'title',
                'category',
                'excerpt',
                'featured_image',
                'image_preview',
                'publish_date',
            ),
            'description': 'These fields appear on the blog card in listing page'
        }),
        
        
        
        ('👤 Author Information', {
            'fields': (
                'author_name',
                'author_role',
                'read_time',
            ),
            'description': 'Author details shown on detail page'
        }),
        
        ('⚙️ Display Settings', {
            'fields': (
                'display_order',
                'is_published',
                'featured',
            ),
            'description': 'Control how the blog appears on website'
        }),
        
                # Add these fieldsets after the existing ones
        
        ('📋 Dynamic Content Sections', {
            'fields': (
                ('show_section_1', 'show_section_2', 'show_section_3', 'show_section_4', 'show_cta'),
            ),
            'description': 'Toggle content sections on/off'
        }),
        
        ('📝 Section 1: Introduction', {
            'fields': (
                'section_1_title',
                'section_1_content',
            ),
            'description': 'First content section - Introduction'
        }),
        
        ('⭐ Section 2: Features (4 Features)', {
            'fields': (
                'section_2_title',
                ('feature_1_title', 'feature_1_icon', 'feature_1_content'),
                ('feature_2_title', 'feature_2_icon', 'feature_2_content'),
                ('feature_3_title', 'feature_3_icon', 'feature_3_content'),
                ('feature_4_title', 'feature_4_icon', 'feature_4_content'),
            ),
            'description': 'Four feature cards with icons'
        }),
        
        ('📋 Section 3: Applications', {
            'fields': (
                'section_3_title',
                'application_1',
                'application_2',
                'application_3',
                'application_4',
                'application_5',
            ),
            'description': 'Application list items'
        }),
        
        ('📊 Section 4: Career Impact', {
            'fields': (
                'section_4_title',
                'section_4_content',
                ('stat_1_number', 'stat_1_text'),
                ('stat_2_number', 'stat_2_text'),
                ('stat_3_number', 'stat_3_text'),
            ),
            'description': 'Career impact with statistics'
        }),
        
        ('🎯 Call to Action', {
            'fields': (
                'cta_title',
                'cta_description',
                'cta_button_text',
                'cta_button_link',
            ),
            'description': 'Call to action section at the end'
        }),
        
        
                # Add these fieldsets after the CTA section
        
        ('🔗 Social Share Section', {
            'fields': (
                'show_social_share',
                'social_share_title',
                'social_share_description',
                ('show_facebook_share', 'show_twitter_share', 'show_linkedin_share'),
            ),
            'description': 'Social share buttons configuration'
        }),
        
        ('🧭 Blog Navigation', {
            'fields': (
                'show_blog_navigation',
                ('previous_nav_label', 'previous_nav_text', 'previous_nav_link', 'is_previous_external'),
                ('next_nav_label', 'next_nav_text', 'next_nav_link', 'is_next_external'),
            ),
            'description': 'Navigation between blog posts'
        }),
        
        
                # Add these fieldsets after the CTA section
        
        ('📋 Sidebar Sections', {
            'fields': (
                ('show_social_section', 'show_courses_section', 'show_categories_section'),
            ),
            'description': 'Toggle sidebar sections on/off'
        }),
        
        ('📱 Social Media Section', {
            'fields': (
                'social_section_title',
                'social_description',
                'instagram_url',
                'facebook_url',
                'linkedin_url',
            ),
            'description': 'Social media links in sidebar'
        }),
        
        ('📚 Related Courses Section', {
            'fields': (
                'courses_section_title',
                ('course_1_title', 'course_1_description', 'course_1_link'),
                ('course_2_title', 'course_2_description', 'course_2_link'),
                ('course_3_title', 'course_3_description', 'course_3_link'),
            ),
            'description': 'Three related courses in sidebar'
        }),
        
        ('📊 Blog Categories Section', {
            'fields': (
                'categories_section_title',
                ('excel_count', 'sql_count', 'python_count', 'azure_count', 'career_count'),
            ),
            'description': 'Blog category counts in sidebar'
        }),
    )
    
    # === READONLY FIELDS ===
    readonly_fields = ['image_preview']
    
    # === CUSTOM METHODS ===
    def image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px; border-radius: 4px; border: 1px solid #ddd;" />',
                obj.featured_image.url
            )
        return "No image uploaded"
    image_preview.short_description = 'Image Preview'
    
    
    


from django.contrib import admin
from .models import HeroSlide

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")




from django.contrib import admin
from django.utils.html import format_html
from django.forms import Textarea
from .models import Advisor


@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Advisors / Mentors.
    Designed to be simple and non-technical for HR users.
    """

    list_display = (
        'name',
        'subtitle_preview',
        'display_order',
        'is_active',
        'created_at',
    )
    list_filter = ('is_active',)
    search_fields = ('name', 'subtitle', 'bio_part1')
    list_editable = ('display_order',)
    actions = ('activate_advisors', 'deactivate_advisors')

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name',
                'subtitle',
                'title',
                'image',
            ),
            'description': (
                'Enter the advisor’s name, role, and profile image. '
                'Subtitle is optional.'
            )
        }),

        ('Biography', {
            'fields': (
                'bio_part1',
                'bio_part2',
            ),
            'description': (
                'Write the main biography content in 2 short paragraphs. '
                'Use third-person language (He / She).'
            )
        }),

        ('Read More Content (Optional)', {
            'fields': (
                'bio_hidden1',
                'bio_hidden2',
            ),
            'description': (
                'Additional information shown when users click “Read More”. '
                'You may leave this empty.'
            ),
            'classes': ('collapse',),
        }),

        ('Highlight Keywords', {
            'fields': ('keywords_to_highlight',),
            'description': (
                'Enter important words or phrases you want to highlight on the website.\n\n'
                '• One keyword or phrase per line\n'
                '• Keywords must already exist in the biography text\n'
                '• These words will appear highlighted automatically'
            ),
            'classes': ('collapse',),
        }),

        ('Display Settings', {
            'fields': (
                'display_order',
                'is_active',
            ),
            'description': (
                'Control visibility and ordering on the website.'
            )
        }),
    )

    # ---------- LIST DISPLAY HELPERS ----------

    def subtitle_preview(self, obj):
        if obj.subtitle:
            return obj.subtitle[:60] + "..." if len(obj.subtitle) > 60 else obj.subtitle
        return "-"
    subtitle_preview.short_description = "Subtitle"

    # ---------- ACTIONS ----------

    def activate_advisors(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f"{updated} advisor(s) activated.")

    activate_advisors.short_description = "Activate selected advisors"

    def deactivate_advisors(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} advisor(s) deactivated.")

    deactivate_advisors.short_description = "Deactivate selected advisors"

    # ---------- FORM CUSTOMIZATION ----------

    formfield_overrides = {
        Textarea: {
            'widget': Textarea(attrs={
                'rows': 4,
                'style': 'width: 100%;'
            })
        }
    }

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Simple, clear help text for subtitle
        if 'subtitle' in form.base_fields:
            form.base_fields['subtitle'].help_text = (
                'Optional. Use • to separate roles.\n'
                'Example: Visiting Professor • AI & Data Science Advisor'
            )

        return form




from django.contrib import admin
from django.utils.html import format_html
from .models import PlacementsSection, CompanyLogo, ManyMoreCompanies


class CompanyLogoInline(admin.TabularInline):
    """Inline editor for company logos"""
    model = CompanyLogo
    extra = 3
    fields = ['company_name', 'logo', 'display_order', 'is_active']
    readonly_fields = ['logo_preview']
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="max-height: 40px; max-width: 80px; border-radius: 4px;" />',
                obj.logo.url
            )
        return "No logo uploaded"
    logo_preview.short_description = 'Preview'


class ManyMoreCompaniesInline(admin.StackedInline):
    """Inline editor for 'Many More' section"""
    model = ManyMoreCompanies
    can_delete = False
    max_num = 1
    min_num = 1
    verbose_name_plural = "'And Many More' Section"
    
    fields = ['additional_count', 'label', 'is_active']
    help_texts = {
        'additional_count': 'Number of additional companies (e.g., 40)',
        'label': 'Text below the count (e.g., Leading Companies)',
    }
    
    

    

@admin.register(PlacementsSection)
class PlacementsSectionAdmin(admin.ModelAdmin):
    """Admin for Placements Sections"""
    
    list_display = [
        'title',
        'companies_display',
        'students_display',
        'sectors_display',
        'is_active',
        'display_order'
    ]
    
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']
    list_editable = ['is_active', 'display_order']
    
    fieldsets = (
        ('📋 Placements Section Content', {
            'fields': (
                'title',
                'subtitle',
                'companies_count',
                'students_placed',
                'sectors_count',
                'display_order',
                'is_active',
            ),
            'description': 'All content and settings for the placements section'
        }),
    )
    
    inlines = [
        CompanyLogoInline, 
        ManyMoreCompaniesInline,
       
        ]
    
    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }
        


from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import InternshipSection, InternshipBenefit


class InternshipBenefitInline(admin.TabularInline):
    model = InternshipBenefit
    extra = 3
    fields = (
        "title",
        "description",
        "icon",
        "icon_color",
    )
    classes = ["wide"]


@admin.register(InternshipSection)
class InternshipSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "partner_companies_display",
        "job_conversion_display",
        "students_placed_display",
        "is_active",
    )

    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("title",)

    formfield_overrides = {
        models.TextField: {
            "widget": Textarea(attrs={"rows": 3, "cols": 60})
        }
    }

    fieldsets = (
        ("Internship Section Content", {
            "fields": (
                "badge_text",
                "title",
                "description",
            )
        }),
        ("Statistics", {
            "fields": (
                "partner_companies",
                "job_conversion_rate",
                "students_placed",
            )
        }),
    )

    inlines = [InternshipBenefitInline]

    def has_add_permission(self, request):
        return not InternshipSection.objects.exists()
