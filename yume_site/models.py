from django.db import models
import re
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ContactInformation(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return "Contact Information"


class Enrollment(models.Model):

    EDUCATION_CHOICES = [
        ('10th', '10th Grade'),
        ('12th', '12th Grade'),
        ('diploma', 'Diploma'),
        ('bsc_cs', 'B.Sc Computer Science'),
        ('bsc_it', 'B.Sc IT'),
        ('bca', 'BCA'),
        ('bcom', 'B.Com'),
        ('btech', 'B.Tech'),
        ('post_graduate', 'Post Graduate'),
        ('other', 'Other'),
    ]

    COURSE_CHOICES = [
        ('Excel for Data Analysis', 'Excel for Data Analysis'),
        ('SQL for Data Analysis', 'SQL for Data Analysis'),
        ('Python Development', 'Python Development'),
        ('Data Visualization', 'Data Visualization'),
        ('Azure Fundamentals', 'Azure Fundamentals'),
        ('Azure AI Fundamentals', 'Azure AI Fundamentals'),
        ('Power Platform', 'Power Platform'),
        ('Security & Compliance', 'Security & Compliance'),
        ('Professional Development', 'Professional Development'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    education = models.CharField(max_length=50, choices=EDUCATION_CHOICES)
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.course}"



class Enquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.email}"







class ProjectCard(models.Model):
    """Model for PROJECT CARDS only (no detailed content)"""
    
    # === BASIC FIELDS FOR CARD ===
    project_name = models.CharField(
        max_length=200,
        help_text="Enter the project name (e.g., ASPIRE Project)"
    )
    
    tagline = models.CharField(
        max_length=300,
        help_text="Short catchy phrase about the project"
    )
    
    category = models.CharField(
        max_length=100,
        help_text="e.g., Technology Training, Government Program"
    )
    
    duration = models.CharField(
        max_length=50,
        help_text="e.g., 120 Hours, 50 Hours, 1-2 Weeks"
    )
    
    # === CARD IMAGE ===
    thumbnail_image = models.ImageField(
        upload_to='projects/card_images/',
        help_text="Image for project card (300x200px recommended)"
    )
    
    # === CARD CONTENT ===
    short_description = models.TextField(
        help_text="Brief description for project card",
        max_length=150
    )
    
    # === DISPLAY SETTINGS ===
    display_order = models.IntegerField(
        default=0,
        help_text="Order in which projects appear (0 = first, 1 = second, etc.)"
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="Show this project card on website"
    )
    
    # === AUTO-GENERATED (hidden from admin) ===
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = "Project Card"
        verbose_name_plural = "Project Cards"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.project_name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.project_name


class ProjectDetail(models.Model):
    """Model for PROJECT DETAIL PAGES only"""
    
    # Icon choices for non-coders
    ICON_CHOICES = [
        ('bi-building', '🏢 Building (Organization)'),
        ('bi-shield-check', '🛡️ Shield (Security/Knowledge)'),
        ('bi-handshake', '🤝 Handshake (Partnership)'),
        ('bi-people', '👥 People (Team/Community)'),
        ('bi-briefcase', '💼 Briefcase (Business)'),
        ('bi-lightbulb', '💡 Lightbulb (Innovation)'),
        ('bi-graph-up', '📈 Graph (Growth)'),
        ('bi-award', '🏆 Award (Excellence)'),
        ('bi-globe', '🌐 Globe (Global/Network)'),
        ('bi-cash-coin', '💰 Money (Funding/CSR)'),
        ('bi-book', '📚 Book (Knowledge/Education)'),
        ('bi-gear', '⚙️ Gear (Technology)'),
        ('bi-heart', '❤️ Heart (Social/CSR)'),
        ('bi-star', '⭐ Star (Quality/Excellence)'),
        ('bi-flag', '🚩 Flag (Government/Initiative)'),
    ]
    
    COLOR_CHOICES = [
        ('primary', '🔵 Blue (Primary)'),
        ('success', '🟢 Green (Success)'),
        ('info', '🔵 Light Blue (Info)'),
        ('warning', '🟡 Yellow (Warning)'),
        ('danger', '🔴 Red (Danger)'),
        ('secondary', '⚫ Gray (Secondary)'),
    ]
    
    # Link to card (one-to-one relationship)
    project_card = models.OneToOneField(
        ProjectCard,
        on_delete=models.CASCADE,
        related_name='detail_page',
        help_text="Select the project card this detail page belongs to"
    )
    
    # === DETAIL PAGE HEADER ===
    badge_text = models.CharField(
        max_length=100,
        default='Skill Development Program',
        help_text="Badge text in header"
    )
    
    launch_date_badge = models.CharField(
        max_length=100,
        default='July 2025 Launch',
        help_text="Launch date badge",
        blank=True
    )
    
    # === DETAIL PAGE METRICS ===
    duration_hours = models.CharField(
        max_length=50,
        default='120 Hours',
        help_text="Duration for metrics section"
    )
    
    student_count = models.IntegerField(
        default=300,
        help_text="Number of students for metrics"
    )
    
    location = models.CharField(
        max_length=100,
        default='Bengaluru',
        help_text="Location for metrics"
    )
    
    # === HERO IMAGE ===
    hero_image = models.ImageField(
        upload_to='projects/hero_images/',
        help_text="Large image for project detail page (optional - uses card image if empty)",
        blank=True,
        null=True
    )
    
    # === TARGET AUDIENCE ===
    target_audience = models.TextField(
        help_text="Target audience description",
        blank=True
    )
    
    # === PARTNERS SECTION ===
    show_partners = models.BooleanField(
        default=True,
        help_text="Show partners section on detail page"
    )
    
    # === PARTNER 1 ===
    partner_1_name = models.CharField(
        max_length=100,
        default='YuMe Learning',
        help_text="First partner organization name",
        blank=True
    )
    
    partner_1_type = models.CharField(
        max_length=100,
        default='Implementing Partner',
        help_text="First partner type/role",
        blank=True
    )
    
    partner_1_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-building',
        help_text="Select an icon for first partner"
    )
    
    partner_1_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='primary',
        help_text="Select color for first partner"
    )
    
    # === PARTNER 2 ===
    partner_2_name = models.CharField(
        max_length=100,
        default='NASSCOM',
        help_text="Second partner organization name",
        blank=True
    )
    
    partner_2_type = models.CharField(
        max_length=100,
        default='Knowledge Partner',
        help_text="Second partner type/role",
        blank=True
    )
    
    partner_2_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-shield-check',
        help_text="Select an icon for second partner"
    )
    
    partner_2_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='success',
        help_text="Select color for second partner"
    )
    
    # === PARTNER 3 ===
    partner_3_name = models.CharField(
        max_length=100,
        default='ITC',
        help_text="Third partner organization name",
        blank=True
    )
    
    partner_3_type = models.CharField(
        max_length=100,
        default='CSR Partner',
        help_text="Third partner type/role",
        blank=True
    )
    
    partner_3_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-handshake',
        help_text="Select an icon for third partner"
    )
    
    partner_3_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='info',
        help_text="Select color for third partner"
    )
    
    # === DETAILED CONTENT ===
    detailed_content = models.TextField(
        help_text="Full project details for the detail page",
        blank=True
    )
    
        # === PROGRAM OVERVIEW SECTION ===
    program_overview_title = models.CharField(
        max_length=200,
        default='Program Overview',
        help_text="Title for program overview section",
        blank=True
    )
    
    program_overview_content = models.TextField(
        help_text="Main content for program overview section",
        blank=True
    )
    
    implementing_partner_name = models.CharField(
        max_length=100,
        default='YuMe Learning',
        help_text="Name of implementing partner",
        blank=True
    )
    
    partner_2_name_overview = models.CharField(
        max_length=100,
        default='NASSCOM Foundation',
        help_text="Name of second partner",
        blank=True
    )
    
    partner_3_name_overview = models.CharField(
        max_length=100,
        default='ITC',
        help_text="Name of third partner",
        blank=True
    )
    
    program_objective = models.TextField(
        help_text="Program objective/description",
        blank=True
    )
    
    learning_approach_title = models.CharField(
        max_length=100,
        default='Learning Approach',
        help_text="Title for learning approach box",
        blank=True
    )
    
    learning_approach_main = models.CharField(
        max_length=100,
        default='Primarily In-person sessions',
        help_text="Main learning approach text",
        blank=True
    )
    
    learning_approach_sub = models.CharField(
        max_length=100,
        default='with occasional online support',
        help_text="Subtext for learning approach",
        blank=True
    )
    
    learning_approach_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-person-video3',
        help_text="Icon for learning approach box"
    )
    
    show_program_overview = models.BooleanField(
        default=True,
        help_text="Show program overview section"
    )
    
    
    
        # === CORE PROGRAM COMPONENTS SECTION ===
    show_program_components = models.BooleanField(
        default=True,
        help_text="Show core program components section"
    )
    
    components_title = models.CharField(
        max_length=200,
        default='Core Program Components',
        help_text="Title for program components section",
        blank=True
    )
    
    # === COMPONENT 1 - Technical Skills ===
    component_1_title = models.CharField(
        max_length=100,
        default='Technical Skills',
        help_text="Title for first component",
        blank=True
    )
    
    component_1_subtitle = models.CharField(
        max_length=100,
        default='Programming & Development',
        help_text="Subtitle for first component",
        blank=True
    )
    
    component_1_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-code-slash',
        help_text="Icon for first component"
    )
    
    component_1_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='primary',
        help_text="Color for first component"
    )
    
    component_1_items = models.TextField(
        help_text="List items for first component (one per line)",
        default="Python Programming\nFull Stack Development\nData Analytics\nSQL Database Management\nReal Dataset Problem-solving",
        blank=True
    )
    
    # === COMPONENT 2 - Hands-on Projects ===
    component_2_title = models.CharField(
        max_length=100,
        default='Hands-on Projects',
        help_text="Title for second component",
        blank=True
    )
    
    component_2_subtitle = models.CharField(
        max_length=100,
        default='Practical Experience',
        help_text="Subtitle for second component",
        blank=True
    )
    
    component_2_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-laptop',
        help_text="Icon for second component"
    )
    
    component_2_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='success',
        help_text="Color for second component"
    )
    
    component_2_items = models.TextField(
        help_text="List items for second component (one per line)",
        default="Weekly Lab Sessions\nIndustry Mini-Projects\nCapstone Project\nTeam-based Simulations\nContinuous Assessment",
        blank=True
    )
    
    # === COMPONENT 3 - Career Development ===
    component_3_title = models.CharField(
        max_length=100,
        default='Career Readiness',
        help_text="Title for third component",
        blank=True
    )
    
    component_3_subtitle = models.CharField(
        max_length=100,
        default='Professional Development',
        help_text="Subtitle for third component",
        blank=True
    )
    
    component_3_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-briefcase',
        help_text="Icon for third component"
    )
    
    component_3_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='warning',
        help_text="Color for third component"
    )
    
    component_3_items = models.TextField(
        help_text="List items for third component (one per line)",
        default="Resume & Portfolio Building\nLinkedIn Optimization\nMock Interview Sessions\nProfessional Communication\nIndustry Networking",
        blank=True
    )
    
    
    
        # === ROLE & IMPACT SECTION ===
    show_role_impact = models.BooleanField(
        default=True,
        help_text="Show role and impact section"
    )
    
    # === ROLE OF IMPLEMENTING PARTNER ===
    role_title = models.CharField(
        max_length=200,
        default='Role of YuMe Learning',
        help_text="Title for role section",
        blank=True
    )
    
    role_description = models.TextField(
        help_text="Description of implementing partner role",
        default="As the implementing partner, YuMe Learning is responsible for comprehensive program delivery and outcome measurement across multiple regions in Karnataka.",
        blank=True
    )
    
    # Role items
    role_item_1_title = models.CharField(
        max_length=100,
        default='Program Delivery',
        help_text="First role item title",
        blank=True
    )
    
    role_item_1_subtitle = models.CharField(
        max_length=100,
        default='Training execution & management',
        help_text="First role item subtitle",
        blank=True
    )
    
    role_item_1_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-gear',
        help_text="Icon for first role item"
    )
    
    role_item_1_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='primary',
        help_text="Color for first role item"
    )
    
    role_item_2_title = models.CharField(
        max_length=100,
        default='Learner Engagement',
        help_text="Second role item title",
        blank=True
    )
    
    role_item_2_subtitle = models.CharField(
        max_length=100,
        default='Student support & monitoring',
        help_text="Second role item subtitle",
        blank=True
    )
    
    role_item_2_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-people',
        help_text="Icon for second role item"
    )
    
    role_item_2_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='success',
        help_text="Color for second role item"
    )
    
    role_item_3_title = models.CharField(
        max_length=100,
        default='Outcome Measurement',
        help_text="Third role item title",
        blank=True
    )
    
    role_item_3_subtitle = models.CharField(
        max_length=100,
        default='Impact assessment & reporting',
        help_text="Third role item subtitle",
        blank=True
    )
    
    role_item_3_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-graph-up',
        help_text="Icon for third role item"
    )
    
    role_item_3_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='info',
        help_text="Color for third role item"
    )
    
    role_item_4_title = models.CharField(
        max_length=100,
        default='Multi-region Implementation',
        help_text="Fourth role item title",
        blank=True
    )
    
    role_item_4_subtitle = models.CharField(
        max_length=100,
        default='Statewide program coverage',
        help_text="Fourth role item subtitle",
        blank=True
    )
    
    role_item_4_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-geo-alt',
        help_text="Icon for fourth role item"
    )
    
    role_item_4_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='warning',
        help_text="Color for fourth role item"
    )
    
    # === PROGRAM IMPACT ===
    impact_title = models.CharField(
        max_length=200,
        default='Program Impact',
        help_text="Title for impact section",
        blank=True
    )
    
    impact_main_number = models.CharField(
        max_length=50,
        default='2,500+',
        help_text="Main impact number",
        blank=True
    )
    
    impact_main_text = models.CharField(
        max_length=100,
        default='Students Trained',
        help_text="Text for main impact number",
        blank=True
    )
    
    # Impact metrics
    impact_metric_1_number = models.CharField(
        max_length=50,
        default='5+',
        help_text="First impact metric number",
        blank=True
    )
    
    impact_metric_1_text = models.CharField(
        max_length=100,
        default='Regions',
        help_text="First impact metric text",
        blank=True
    )
    
    impact_metric_2_number = models.CharField(
        max_length=50,
        default='50',
        help_text="Second impact metric number",
        blank=True
    )
    
    impact_metric_2_text = models.CharField(
        max_length=100,
        default='Hours/Student',
        help_text="Second impact metric text",
        blank=True
    )
    
    # Outcome progress bars
    outcome_1_label = models.CharField(
        max_length=100,
        default='Skill Enhancement',
        help_text="First outcome label",
        blank=True
    )
    
    outcome_1_value = models.IntegerField(
        default=94,
        help_text="First outcome percentage (0-100)",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    
    outcome_1_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='success',
        help_text="Color for first outcome progress bar"
    )
    
    outcome_2_label = models.CharField(
        max_length=100,
        default='Employability',
        help_text="Second outcome label",
        blank=True
    )
    
    outcome_2_value = models.IntegerField(
        default=89,
        help_text="Second outcome percentage (0-100)",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    
    outcome_2_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='warning',
        help_text="Color for second outcome progress bar"
    )
    
    outcome_3_label = models.CharField(
        max_length=100,
        default='Student Satisfaction',
        help_text="Third outcome label",
        blank=True
    )
    
    outcome_3_value = models.IntegerField(
        default=96,
        help_text="Third outcome percentage (0-100)",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    
    outcome_3_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='info',
        help_text="Color for third outcome progress bar"
    )
    
    
        # === CERTIFICATION & SUPPORT SECTION ===
    show_certification_support = models.BooleanField(
        default=True,
        help_text="Show certification and support section"
    )
    
    # === CERTIFICATION CARD ===
    certification_title = models.CharField(
        max_length=200,
        default='Industry Certification',
        help_text="Title for certification card",
        blank=True
    )
    
    certification_subtitle = models.CharField(
        max_length=200,
        default='Validated by NASSCOM Foundation',
        help_text="Subtitle for certification card",
        blank=True
    )
    
    certification_description = models.TextField(
        help_text="Description for certification card",
        default='Industry-recognized certification validating technical competencies and employability skills.',
        blank=True
    )
    
    certification_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-award',
        help_text="Icon for certification card"
    )
    
    certification_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='primary',
        help_text="Color for certification card"
    )
    
    # Certification features (4 items)
    cert_feature_1_text = models.CharField(
        max_length=100,
        default='Technical Validation',
        help_text="First certification feature",
        blank=True
    )
    
    cert_feature_1_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-check-circle',
        help_text="Icon for first feature"
    )
    
    cert_feature_1_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='success',
        help_text="Color for first feature"
    )
    
    cert_feature_2_text = models.CharField(
        max_length=100,
        default='Employability Proof',
        help_text="Second certification feature",
        blank=True
    )
    
    cert_feature_2_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-person-check',
        help_text="Icon for second feature"
    )
    
    cert_feature_2_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='primary',
        help_text="Color for second feature"
    )
    
    cert_feature_3_text = models.CharField(
        max_length=100,
        default='Industry Recognition',
        help_text="Third certification feature",
        blank=True
    )
    
    cert_feature_3_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-award',
        help_text="Icon for third feature"
    )
    
    cert_feature_3_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='warning',
        help_text="Color for third feature"
    )
    
    cert_feature_4_text = models.CharField(
        max_length=100,
        default='Career Readiness Support',
        help_text="Fourth certification feature",
        blank=True
    )
    
    cert_feature_4_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-briefcase',
        help_text="Icon for fourth feature"
    )
    
    cert_feature_4_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='info',
        help_text="Color for fourth feature"
    )
    
    # === SUPPORT CARD ===
    support_title = models.CharField(
        max_length=200,
        default='Placement Support',
        help_text="Title for support card",
        blank=True
    )
    
    support_subtitle = models.CharField(
        max_length=200,
        default='End-to-end Career Assistance',
        help_text="Subtitle for support card",
        blank=True
    )
    
    support_description = models.TextField(
        help_text="Description for support card",
        default='Comprehensive placement and internship support with industry connections.',
        blank=True
    )
    
    support_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-briefcase',
        help_text="Icon for support card"
    )
    
    support_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='success',
        help_text="Color for support card"
    )
    
    # Support features (4 items)
    support_feature_1_text = models.CharField(
        max_length=100,
        default='Industry Connect',
        help_text="First support feature",
        blank=True
    )
    
    support_feature_1_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-building',
        help_text="Icon for first feature"
    )
    
    support_feature_1_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='info',
        help_text="Color for first feature"
    )
    
    support_feature_2_text = models.CharField(
        max_length=100,
        default='Mock Interviews',
        help_text="Second support feature",
        blank=True
    )
    
    support_feature_2_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-chat-dots',
        help_text="Icon for second feature"
    )
    
    support_feature_2_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='warning',
        help_text="Color for second feature"
    )
    
    support_feature_3_text = models.CharField(
        max_length=100,
        default='Mentorship',
        help_text="Third support feature",
        blank=True
    )
    
    support_feature_3_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-people',
        help_text="Icon for third feature"
    )
    
    support_feature_3_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='secondary',
        help_text="Color for third feature"
    )
    
    support_feature_4_text = models.CharField(
        max_length=100,
        default='Career Guidance',
        help_text="Fourth support feature",
        blank=True
    )
    
    support_feature_4_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-graph-up',
        help_text="Icon for fourth feature"
    )
    
    support_feature_4_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='danger',
        help_text="Color for fourth feature"
    )
    
    
        # === SUSTAINABLE PATHWAYS SECTION ===
    show_sustainable_pathways = models.BooleanField(
        default=True,
        help_text="Show sustainable pathways section"
    )
    
    # Main content
    pathways_title = models.CharField(
        max_length=200,
        default='Creating Sustainable Career Pathways',
        help_text="Title for sustainable pathways section",
        blank=True
    )
    
    pathways_description = models.TextField(
        help_text="Description for sustainable pathways section",
        default='The ASPIRE Project is more than a training program — it is a career enablement initiative. By combining technical excellence, professional skills, mentorship, and industry partnerships, YuMe Learning, along with NASSCOM Foundation and ITC, is enabling students to transition successfully from classrooms to careers.',
        blank=True
    )
    
    # Partner badges (3 badges)
    partner_badge_1_name = models.CharField(
        max_length=100,
        default='YuMe Learning',
        help_text="First partner badge name",
        blank=True
    )
    
    partner_badge_1_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-building',
        help_text="Icon for first partner badge"
    )
    
    partner_badge_1_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='primary',
        help_text="Color for first partner badge"
    )
    
    partner_badge_2_name = models.CharField(
        max_length=100,
        default='NASSCOM Foundation',
        help_text="Second partner badge name",
        blank=True
    )
    
    partner_badge_2_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-shield-check',
        help_text="Icon for second partner badge"
    )
    
    partner_badge_2_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='success',
        help_text="Color for second partner badge"
    )
    
    partner_badge_3_name = models.CharField(
        max_length=100,
        default='ITC',
        help_text="Third partner badge name",
        blank=True
    )
    
    partner_badge_3_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-handshake',
        help_text="Icon for third partner badge"
    )
    
    partner_badge_3_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='info',
        help_text="Color for third partner badge"
    )
    
    # Program highlights
    highlights_title = models.CharField(
        max_length=200,
        default='Program Highlights',
        help_text="Title for highlights box",
        blank=True
    )
    
    highlight_1_text = models.CharField(
        max_length=200,
        default='Industry-Aligned Curriculum',
        help_text="First highlight text",
        blank=True
    )
    
    highlight_1_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='success',
        help_text="Color for first highlight"
    )
    
    highlight_2_text = models.CharField(
        max_length=200,
        default='Hands-on Practical Experience',
        help_text="Second highlight text",
        blank=True
    )
    
    highlight_2_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='primary',
        help_text="Color for second highlight"
    )
    
    highlight_3_text = models.CharField(
        max_length=200,
        default='Mentorship & Career Guidance',
        help_text="Third highlight text",
        blank=True
    )
    
    highlight_3_color = models.CharField(
        max_length=30,
        choices=COLOR_CHOICES,
        default='warning',
        help_text="Color for third highlight"
    )
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Project Detail Page"
        verbose_name_plural = "Project Detail Pages"
    
    def __str__(self):
        return f"Detail page for {self.project_card.project_name}"
    
    @property
    def student_count_display(self):
        """Format student count with + sign"""
        return f"{self.student_count}+"






class Course(models.Model):
    # =============================
    # COURSE CARD (LISTING PAGE)
    # =============================
    title = models.CharField(max_length=200)
    card_description = models.TextField(
        blank=True,
        help_text="Shown only on course cards"
    )
    image = models.ImageField(upload_to='courses/')

    # =============================
    # COURSE DETAIL PAGE (HERO)
    # =============================
    subtitle = models.CharField(
        max_length=255,
        blank=True,
        help_text="Shown below course title"
    )
    overview = models.TextField(
        blank=True,
        help_text="Main description for course detail page"
    )
    duration = models.CharField(max_length=50, blank=True)
    total_hours = models.CharField(max_length=50, blank=True)
    level = models.CharField(max_length=100, blank=True)
    format = models.CharField(max_length=100, blank=True)
    whatsapp_number = models.CharField(
        max_length=20,
        blank=True,
        help_text="Example: 918792885644"
    )
    contact_number = models.CharField(
        max_length=20,
        blank=True,
        help_text="Shown below enrollment card"
    )
    course_url = models.CharField(max_length=100, unique=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CourseHighlight(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="highlights"
    )

    ICON_CHOICES = [
        ("bi bi-code-slash", "Coding & Functions"),
        ("bi bi-bar-chart-steps", "Charts & Analytics"),
        ("bi bi-folder-check", "Hands-on Projects"),
        ("bi bi-people", "Mentor Support"),
        ("bi bi-award", "Certification"),
        ("bi bi-laptop", "Online Learning"),
        ("bi bi-clock-history", "Flexible Timing"),
        ("bi bi-briefcase", "Career Focused"),
        ("bi bi-lightning-charge", "Fast Track"),
        ("bi bi-patch-check", "Industry Ready"),
    ]

    icon_class = models.CharField(
        max_length=100,
        choices=ICON_CHOICES,
        default="bi bi-code-slash",
        verbose_name="Icon"
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.course.title} – {self.title}"


class CurriculumMonth(models.Model):
    COLOR_CHOICES = [
        ("primary", "Blue"),
        ("success", "Green"),
        ("warning", "Yellow"),
        ("danger", "Red"),
        ("info", "Light Blue"),
        ("secondary", "Gray"),
        ("dark", "Dark"),
    ]

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="curriculum_months",
        help_text="Select which course this month belongs to"
    )
    title = models.CharField(
        max_length=50,
        help_text="Example: Month 1, Month 2"
    )
    subtitle = models.CharField(
        max_length=255,
        help_text="Example: Excel Foundations & Data Basics"
    )
    meta_info = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: 40 Hours • Beginner Level"
    )
    badge_color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default="primary",
        help_text="Choose a color label for this month"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls the display order"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Uncheck to hide this month on website"
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.course.title} – {self.title}"


class CurriculumSection(models.Model):
    month = models.ForeignKey(
        CurriculumMonth,
        on_delete=models.CASCADE,
        related_name="sections",
        help_text="This section belongs to which month"
    )
    
    # ADD THIS: Direct link to Course
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="curriculum_sections",
        null=True,
        blank=True,
        help_text="Course this section belongs to"
    )
    
    title = models.CharField(
        max_length=200,
        help_text="Example: Week 1–2: Core Fundamentals"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls section order inside the month"
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Auto-populate course from month if not set
        if not self.course and self.month:
            self.course = self.month.course
        super().save(*args, **kwargs)


class CurriculumTopic(models.Model):
    section = models.ForeignKey(
        CurriculumSection,
        on_delete=models.CASCADE,
        related_name="topics",
        help_text="This topic belongs to which section"
    )
    
    # ADD THIS: Direct link to Course
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="curriculum_topics",
        null=True,
        blank=True,
        help_text="Course this topic belongs to"
    )
    
    title = models.CharField(
        max_length=255,
        help_text="Example: Excel Interface & Navigation"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls topic order"
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Auto-populate course from section if not set
        if not self.course and self.section:
            self.course = self.section.course
        super().save(*args, **kwargs)

COLOR_CHOICES = [
    ("primary", "Blue"),
    ("success", "Green"),
    ("warning", "Yellow"),
    ("info", "Sky Blue"),
]


class CourseLearningOutcome(models.Model):
    course = models.ForeignKey(
        "Course",
        related_name="learning_outcomes",
        on_delete=models.CASCADE
    )
    title = models.CharField(
        "Outcome Title",
        max_length=255,
        help_text="Example: Data Analysis Mastery"
    )
    description = models.TextField(
        "Short Description",
        help_text="1–2 short lines explaining this outcome"
    )
    color = models.CharField(
        "Dot Color",
        max_length=20,
        choices=COLOR_CHOICES,
        default="primary",
        help_text="Controls the circle & border color on website"
    )
    order = models.PositiveIntegerField(
        "Display Order",
        default=0,
        help_text="Lower number = shows first"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Learning Outcome"
        verbose_name_plural = "Learning Outcomes"

    def __str__(self):
        return self.title


class CourseTool(models.Model):
    course = models.ForeignKey(
        "Course",
        related_name="tools",
        on_delete=models.CASCADE
    )
    name = models.CharField(
        "Tool Name",
        max_length=255,
        help_text="Example: Microsoft Excel"
    )
    description = models.TextField(
        "Usage Description",
        help_text="Explain how this tool is used in the course"
    )
    color = models.CharField(
        "Left Border Color",
        max_length=20,
        choices=COLOR_CHOICES,
        default="primary",
        help_text="Controls the left border color"
    )
    order = models.PositiveIntegerField(
        "Display Order",
        default=0,
        help_text="Lower number = shows first"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Tool / Technology"
        verbose_name_plural = "Tools & Technologies"

    def __str__(self):
        return self.name


class CourseCertificationPoint(models.Model):
    course = models.ForeignKey(
        "Course",
        related_name="certification_points",
        on_delete=models.CASCADE
    )
    text = models.CharField(
        max_length=255,
        help_text="Example: Resume Building Workshop"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls display order"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Certification / Placement Point"
        verbose_name_plural = "Certification & Placement Support"

    def __str__(self):
        return self.text


class CourseFAQ(models.Model):
    course = models.ForeignKey(
        "Course",
        related_name="faqs",
        on_delete=models.CASCADE
    )
    question = models.CharField(
        max_length=255,
        help_text="FAQ Question"
    )
    answer = models.TextField(
        help_text="Detailed answer shown when expanded"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls FAQ order"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "FAQ"
        verbose_name_plural = "Frequently Asked Questions"

    def __str__(self):
        return self.question


CAREER_ICON_CHOICES = [
    ("data", "📊 Data / Analytics"),
    ("finance", "💰 Finance / Money"),
    ("business", "📈 Business / Growth"),
    ("speed", "⚡ Performance / Speed"),
    ("intelligence", "🧠 Intelligence"),
    ("corporate", "🏢 Corporate"),
    ("reporting", "🧮 Reporting"),
    ("tech", "🖥️ IT / Technology"),
]


class CourseCareerOpportunity(models.Model):
    course = models.ForeignKey(
        "Course",
        related_name="career_opportunities",
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=100,
        help_text="Example: Data Analyst"
    )
    description = models.TextField(
        help_text="Example: Entry to Mid-level positions"
    )
    tag = models.CharField(
        max_length=50,
        help_text="Example: High Demand, Growing Field"
    )
    icon_type = models.CharField(
        max_length=20,
        choices=CAREER_ICON_CHOICES,
        default="data",
        help_text="Just select from dropdown (no technical knowledge needed)"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls display order (1, 2, 3...)"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Career Opportunity"
        verbose_name_plural = "Career Opportunities"

    def __str__(self):
        return self.title




ICON_CHOICES = [
    ('bi-table', 'Table'),
    ('bi-lightning-charge', 'Lightning'),
    ('bi-graph-up', 'Graph Up'),
    ('bi-bar-chart', 'Bar Chart'),
    ('bi-briefcase', 'Briefcase'),
    ('bi-cash-coin', 'Money'),
    ('bi-people', 'People'),
    ('bi-gear', 'Gear'),
    ('bi-check-circle', 'Check Circle'),
    ('bi-star', 'Star'),
    ('bi-award', 'Award'),
    ('bi-clock', 'Clock'),
    ('bi-calendar', 'Calendar'),
    ('bi-chat', 'Chat'),
    ('bi-book', 'Book'),
    ('bi-laptop', 'Laptop'),
    ('bi-code', 'Code'),
    ('bi-shield', 'Shield'),
    ('bi-globe', 'Globe'),
    ('bi-heart', 'Heart'),
]


# Update the DynamicBlog class in your existing models.py
class DynamicBlog(models.Model):
    """Model for blogs only"""
    
    # Category choices (without emojis)
    CATEGORY_CHOICES = [
        ('excel', 'Excel'),
        ('sql', 'SQL'),
        ('python', 'Python'),
        ('data_viz', 'Data Visualization'),
        ('azure', 'Azure'),
        ('ai_ml', 'AI & ML'),
        ('power_platform', 'Power Platform'),
        ('security', 'Security'),
        ('soft_skills', 'Soft Skills'),
        ('tech_training', 'Technology Training'),
        ('career', 'Career Development'),
    ]
    
    # === BLOG CARD FIELDS (Basic Information) ===
    title = models.CharField(
        max_length=200,
        help_text="Enter blog post title"
    )
    
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='tech_training',
        help_text="Select blog category"
    )
    
    excerpt = models.TextField(
        max_length=200,
        help_text="Short description for blog card (max 200 characters)"
    )
    
    featured_image = models.ImageField(
        upload_to='blog/featured_images/',
        help_text="Image for blog card (700x400px recommended)"
    )
    
    publish_date = models.DateField(
        help_text="Select publish date for blog"
    )
    
    # === BLOG DETAIL PAGE FIELDS ===
    author_name = models.CharField(
        max_length=100,
        default='YuMe Learning Team',
        help_text="Author name"
    )
    
    author_role = models.CharField(
        max_length=100,
        default='Professional Development Experts',
        help_text="Author role/designation"
    )
    
    read_time = models.CharField(
        max_length=50,
        default='5 min read',
        help_text="Estimated reading time (e.g., 5 min read, 10 min read)"
    )
    
   
    
    # === DISPLAY SETTINGS ===
    is_published = models.BooleanField(
        default=True,
        help_text="Show this blog on website"
    )
    
    featured = models.BooleanField(
        default=False,
        help_text="Feature this blog on homepage"
    )
    
    display_order = models.IntegerField(
        default=0,
        help_text="Order in which blogs appear (0 = first, 1 = second)"
    )
    
    # Auto-generated fields
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True
    )
    
    
        # === DYNAMIC CONTENT SECTIONS ===
    # Section 1: Why Section
    section_1_title = models.CharField(
        max_length=200,
        default='Why Excel is Essential',
        help_text="Title for first content section",
        blank=True
    )
    
    section_1_content = models.TextField(
        help_text="Content for first section",
        default='Microsoft Excel remains one of the most powerful tools for data analysis in today\'s business environment. Despite new tools, Excel\'s versatility and accessibility make it indispensable for professionals.\n\nAt Yume Learning, we focus on practical, industry-aligned skills. Our Excel for Data Analysis course transforms theoretical knowledge into market-ready expertise that employers seek.',
        blank=True
    )
    
    # Section 2: Features Section
    section_2_title = models.CharField(
        max_length=200,
        default='Advanced Features to Master',
        help_text="Title for second content section",
        blank=True
    )
    
    # Feature 1
    feature_1_title = models.CharField(
        max_length=100,
        default='Pivot Tables',
        help_text="First feature title",
        blank=True
    )
    
    feature_1_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-table',
        help_text="Icon for first feature"
    )
    
    feature_1_content = models.TextField(
        max_length=200,
        default='Transform data into insights, create dynamic reports, and use slicers for interactive filtering.',
        help_text="Description for first feature",
        blank=True
    )
    
    # Feature 2
    feature_2_title = models.CharField(
        max_length=100,
        default='Power Query',
        help_text="Second feature title",
        blank=True
    )
    
    feature_2_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-lightning-charge',
        help_text="Icon for second feature"
    )
    
    feature_2_content = models.TextField(
        max_length=200,
        default='Automate data cleaning, combine multiple sources, and create repeatable workflows.',
        help_text="Description for second feature",
        blank=True
    )
    
    # Feature 3
    feature_3_title = models.CharField(
        max_length=100,
        default='Advanced Formulas',
        help_text="Third feature title",
        blank=True
    )
    
    feature_3_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-graph-up',
        help_text="Icon for third feature"
    )
    
    feature_3_content = models.TextField(
        max_length=200,
        default='Master INDEX-MATCH, XLOOKUP, dynamic arrays, and statistical functions.',
        help_text="Description for third feature",
        blank=True
    )
    
    # Feature 4
    feature_4_title = models.CharField(
        max_length=100,
        default='Data Visualization',
        help_text="Fourth feature title",
        blank=True
    )
    
    feature_4_icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='bi-bar-chart',
        help_text="Icon for fourth feature"
    )
    
    feature_4_content = models.TextField(
        max_length=200,
        default='Create compelling charts and dashboards that communicate insights effectively.',
        help_text="Description for fourth feature",
        blank=True
    )
    
    # Section 3: Applications Section
    section_3_title = models.CharField(
        max_length=200,
        default='Real-World Applications',
        help_text="Title for third content section",
        blank=True
    )
    
    application_1 = models.CharField(
        max_length=200,
        default='Business Reporting: Create automated dashboards that update with new data',
        help_text="First application",
        blank=True
    )
    
    application_2 = models.CharField(
        max_length=200,
        default='Financial Analysis: Build models with scenario analysis and forecasting',
        help_text="Second application",
        blank=True
    )
    
    application_3 = models.CharField(
        max_length=200,
        default='Sales Tracking: Analyze performance and predict future trends',
        help_text="Third application",
        blank=True
    )
    
    application_4 = models.CharField(
        max_length=200,
        default='Inventory Management: Track stock levels and optimize ordering',
        help_text="Fourth application",
        blank=True
    )
    
    application_5 = models.CharField(
        max_length=200,
        default='Project Management: Create Gantt charts and track project timelines',
        help_text="Fifth application",
        blank=True
    )
    
    # Section 4: Career Impact
    section_4_title = models.CharField(
        max_length=200,
        default='Career Impact',
        help_text="Title for fourth content section",
        blank=True
    )
    
    section_4_content = models.TextField(
        help_text="Content for career impact section",
        default='Excel proficiency is among the top skills employers seek. Industry data shows that our Excel for Data Analysis course bridges classroom theory with industry needs. We focus on hands-on training for real-world challenges.',
        blank=True
    )
    
    # Statistics
    stat_1_number = models.CharField(
        max_length=50,
        default='82%',
        help_text="First statistic number",
        blank=True
    )
    
    stat_1_text = models.CharField(
        max_length=100,
        default='Jobs require Excel',
        help_text="First statistic text",
        blank=True
    )
    
    stat_2_number = models.CharField(
        max_length=50,
        default='35%',
        help_text="Second statistic number",
        blank=True
    )
    
    stat_2_text = models.CharField(
        max_length=100,
        default='Higher productivity',
        help_text="Second statistic text",
        blank=True
    )
    
    stat_3_number = models.CharField(
        max_length=50,
        default='₹6-12L',
        help_text="Third statistic number",
        blank=True
    )
    
    stat_3_text = models.CharField(
        max_length=100,
        default='Salary boost',
        help_text="Third statistic text",
        blank=True
    )
    
    # Call to Action
    cta_title = models.CharField(
        max_length=200,
        default='Ready to Master Excel?',
        help_text="Call to action title",
        blank=True
    )
    
    cta_description = models.CharField(
        max_length=200,
        default='Join our Excel for Data Analysis course today.',
        help_text="Call to action description",
        blank=True
    )
    
    cta_button_text = models.CharField(
        max_length=100,
        default='Explore Course',
        help_text="Button text for call to action",
        blank=True
    )
    
    cta_button_link = models.CharField(
        max_length=200,
        default='/courses/excel-data-analysis',
        help_text="URL for call to action button",
        blank=True
    )
    
    # Toggle sections
    show_section_1 = models.BooleanField(
        default=True,
        help_text="Show first content section"
    )
    
    show_section_2 = models.BooleanField(
        default=True,
        help_text="Show features section"
    )
    
    show_section_3 = models.BooleanField(
        default=True,
        help_text="Show applications section"
    )
    
    show_section_4 = models.BooleanField(
        default=True,
        help_text="Show career impact section"
    )
    
    show_cta = models.BooleanField(
        default=True,
        help_text="Show call to action section"
    )
    
    
    
        # === SOCIAL SHARE SECTION ===
    show_social_share = models.BooleanField(
        default=True,
        help_text="Show social share section"
    )
    
    social_share_title = models.CharField(
        max_length=200,
        default='Share this article',
        help_text="Title for social share section",
        blank=True
    )
    
    social_share_description = models.CharField(
        max_length=200,
        default='Help others discover this valuable content',
        help_text="Description for social share section",
        blank=True
    )
    
    show_facebook_share = models.BooleanField(
        default=True,
        help_text="Show Facebook share button"
    )
    
    show_twitter_share = models.BooleanField(
        default=True,
        help_text="Show Twitter share button"
    )
    
    show_linkedin_share = models.BooleanField(
        default=True,
        help_text="Show LinkedIn share button"
    )
    
    # === BLOG NAVIGATION SECTION ===
    show_blog_navigation = models.BooleanField(
        default=True,
        help_text="Show blog navigation section"
    )
    
    # Previous navigation
    previous_nav_label = models.CharField(
        max_length=100,
        default='Previous',
        help_text="Label for previous navigation",
        blank=True
    )
    
    previous_nav_text = models.CharField(
        max_length=200,
        default='Blog List',
        help_text="Text for previous navigation",
        blank=True
    )
    
    previous_nav_link = models.CharField(
        max_length=200,
        default='blog',
        help_text="URL name or path for previous navigation (e.g., blog for Blog List)",
        blank=True
    )
    
    # Next navigation
    next_nav_label = models.CharField(
        max_length=100,
        default='Next',
        help_text="Label for next navigation",
        blank=True
    )
    
    next_nav_text = models.CharField(
        max_length=200,
        default='SQL for Data Analysis',
        help_text="Text for next navigation",
        blank=True
    )
    
    next_nav_link = models.CharField(
        max_length=200,
        default='sql_blog',
        help_text="URL name or path for next navigation (e.g., sql_blog for SQL Blog)",
        blank=True
    )
    
    is_previous_external = models.BooleanField(
        default=False,
        help_text="Check if previous link is external URL (not Django URL name)"
    )
    
    is_next_external = models.BooleanField(
        default=False,
        help_text="Check if next link is external URL (not Django URL name)"
    )
    
    
    
        # === SIDEBAR SECTIONS ===
    
    # Social Media Section
    show_social_section = models.BooleanField(
        default=True,
        help_text="Show social media section in sidebar"
    )
    
    social_section_title = models.CharField(
        max_length=200,
        default='Follow Yume Learning',
        help_text="Title for social media section",
        blank=True
    )
    
    social_description = models.CharField(
        max_length=200,
        default='Stay updated with courses and career tips',
        help_text="Description under social icons",
        blank=True
    )
    
    # Social Media Links
    instagram_url = models.URLField(
        default='https://www.instagram.com/yumelearning/',
        help_text="Instagram profile URL",
        blank=True
    )
    
    facebook_url = models.URLField(
        default='https://www.facebook.com/yumelearning',
        help_text="Facebook page URL",
        blank=True
    )
    
    linkedin_url = models.URLField(
        default='https://www.linkedin.com/company/antsskillvarsity/',
        help_text="LinkedIn company page URL",
        blank=True
    )
    
    # Related Courses Section
    show_courses_section = models.BooleanField(
        default=True,
        help_text="Show related courses section in sidebar"
    )
    
    courses_section_title = models.CharField(
        max_length=200,
        default='Related Courses',
        help_text="Title for courses section",
        blank=True
    )
    
    # Course 1
    course_1_title = models.CharField(
        max_length=200,
        default='Excel for Data Analysis',
        help_text="First course title",
        blank=True
    )
    
    course_1_description = models.CharField(
        max_length=200,
        default='Learn powerful Excel tools for data analysis',
        help_text="First course description",
        blank=True
    )
    
    course_1_link = models.CharField(
        max_length=200,
        default='/courses/excel-data-analysis',
        help_text="First course URL",
        blank=True
    )
    
    # Course 2
    course_2_title = models.CharField(
        max_length=200,
        default='Data Visualization',
        help_text="Second course title",
        blank=True
    )
    
    course_2_description = models.CharField(
        max_length=200,
        default='Create compelling visualizations',
        help_text="Second course description",
        blank=True
    )
    
    course_2_link = models.CharField(
        max_length=200,
        default='/courses/data-visualization',
        help_text="Second course URL",
        blank=True
    )
    
    # Course 3
    course_3_title = models.CharField(
        max_length=200,
        default='SQL for Data Analysis',
        help_text="Third course title",
        blank=True
    )
    
    course_3_description = models.CharField(
        max_length=200,
        default='Extract and analyze data using SQL',
        help_text="Third course description",
        blank=True
    )
    
    course_3_link = models.CharField(
        max_length=200,
        default='/courses/sql-data-analysis',
        help_text="Third course URL",
        blank=True
    )
    
    # Blog Categories Section
    show_categories_section = models.BooleanField(
        default=True,
        help_text="Show blog categories section in sidebar"
    )
    
    categories_section_title = models.CharField(
        max_length=200,
        default='Blog Categories',
        help_text="Title for categories section",
        blank=True
    )
    
    # Category Counts (for display)
    excel_count = models.IntegerField(
        default=6,
        help_text="Number of Excel blog posts",
        validators=[MinValueValidator(0)]
    )
    
    sql_count = models.IntegerField(
        default=5,
        help_text="Number of SQL blog posts",
        validators=[MinValueValidator(0)]
    )
    
    python_count = models.IntegerField(
        default=4,
        help_text="Number of Python blog posts",
        validators=[MinValueValidator(0)]
    )
    
    azure_count = models.IntegerField(
        default=3,
        help_text="Number of Azure blog posts",
        validators=[MinValueValidator(0)]
    )
    
    career_count = models.IntegerField(
        default=2,
        help_text="Number of Career Tips blog posts",
        validators=[MinValueValidator(0)]
    )
    
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-publish_date']
        verbose_name = "Blog"  # Changed from "Dynamic Blog"
        verbose_name_plural = "Blogs"  # Changed from "Dynamic Blogs"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    @property
    def category_display(self):
        """Get category display name"""
        return dict(self.CATEGORY_CHOICES).get(self.category, self.category)
    
    @property
    def category_color(self):
        """Get category color for badge"""
        category_colors = {
            'excel': '#05c9fe',  # Excel blue
            'sql': '#05c9fe',    # SQL purple
            'python': '#05c9fe',  # Python blue
            'data_viz': '#05c9fe', # Data viz red
            'azure': '#05c9fe',  # Azure blue
            'ai_ml': '#05c9fe',  # AI orange
            'power_platform': '#05c9fe', # Power Platform purple
            'security': '#05c9fe', # Security green
            'soft_skills': '#05c9fe', # Soft skills teal
            'tech_training': '#05c9fe', # Tech training violet
            'career': '#05c9fe', # Career orange
        }
        return category_colors.get(self.category, '#05c9fe')
    
    
    
    
    


class HeroSlide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    image = models.ImageField(upload_to="hero_slides/")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title




class Advisor(models.Model):
    """Model for Advisor/Mentor section"""
    
    # Basic Information
    name = models.CharField(
        max_length=200,
        help_text="Advisor's full name (e.g., Dr. Ravi Shankar)"
    )
    
    subtitle = models.CharField(
        max_length=300,
        help_text="Short description that appears under the name. Use • to separate roles.<br>Example: CO-FOUNDER • ANTS SKILL VARSITY • SOCIAL ENTREPRENEUR • SKILLING LEADER",
        blank=True
    )
    
    image = models.ImageField(
        upload_to='advisors/',
        help_text="Profile photo of the advisor (recommended size: 350x380px, JPG/PNG format)"
    )
    
    title = models.CharField(
        max_length=200,
        default='Advisor & Mentor',
        help_text="Section title that appears above advisor's name",
        blank=True
    )
    
    # Main Content (for Read More section)
    bio_part1 = models.TextField(
        help_text="First paragraph of biography (shown by default)<br><br>Tips for writing:<br>• Start with a strong introduction<br>• Mention their key expertise<br>• Use complete sentences<br><br>Example: Dr. Ravi Shankar is a global thought leader in framing accreditation and certification standards for Data Science & AI-ML."
    )
    
    bio_part2 = models.TextField(
        help_text="Second paragraph of biography (shown by default)<br><br>Tips for writing:<br>• Mention current roles/positions<br>• Include specific institutions<br>• Highlight teaching specialties<br><br>Example: Currently a Visiting Professor at leading business institutes including ISB and Singapore Management University.",
        blank=True
    )
    
    bio_hidden1 = models.TextField(
        help_text="First hidden paragraph (shown when clicking Read More)<br><br>Tips for writing:<br>• Include co-founded ventures<br>• Mention past experiences<br>• Add industry-specific work<br><br>Example: He is actively involved in transforming the sugarcane industry from a net-zero perspective.",
        blank=True
    )
    
    bio_hidden2 = models.TextField(
        help_text="Second hidden paragraph (shown when clicking Read More)<br><br>Tips for writing:<br>• Add mentor/advisor roles<br>• Include board memberships<br>• Mention accelerators/incubators<br><br>Example: A seasoned AgTech mentor associated with multiple accelerators & incubators.",
        blank=True
    )
    
    # Keywords to highlight (for admin reference)
    keywords_to_highlight = models.TextField(
        help_text="<strong>IMPORTANT FOR HR:</strong><br>List keywords that should appear in BLUE color in the text.<br>Enter one keyword per line.<br><br>Example keywords:<br>global thought leader<br>Data Science & AI-ML<br>IR4.0 technologies<br>AI-ML programs for CXOs<br>Visiting Professor<br>ISB<br>Singapore Management University",
        blank=True
    )
    
    # Display Settings
    display_order = models.IntegerField(
        default=0,
        help_text="Order in which advisors appear (0 = first, 1 = second, etc.)"
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="✓ Show this advisor on the website<br>✗ Hide this advisor from the website"
    )
    
    # Dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = "Advisor"
        verbose_name_plural = "Advisors"
    
    def __str__(self):
        return self.name
    
    def get_keywords_list(self):
        """Convert keywords text to list"""
        if self.keywords_to_highlight:
            return [keyword.strip() for keyword in self.keywords_to_highlight.split('\n') if keyword.strip()]
        return []
    
    def highlight_keywords_in_text(self, text):
        """Automatically highlight keywords in the text"""
        if not text:
            return ""
        
        # Get keywords list
        keywords = self.get_keywords_list()
        if not keywords:
            return text
        
        # Process the text to highlight keywords
        processed_text = text
        
        # Sort keywords by length (longest first) to prevent partial matches
        sorted_keywords = sorted(keywords, key=len, reverse=True)
        
        for keyword in sorted_keywords:
            if keyword and len(keyword) > 2:  # Only highlight words longer than 2 characters
                # Create a pattern that matches the whole word
                pattern = r'\b(' + re.escape(keyword) + r')\b'
                # Replace with highlighted span
                processed_text = re.sub(
                    pattern,
                    r'<span class="advisor-highlight">\1</span>',
                    processed_text,
                    flags=re.IGNORECASE
                )
        
        return processed_text
    
    def get_highlighted_bio_part1(self):
        """Get bio part 1 with highlighted keywords"""
        return self.highlight_keywords_in_text(self.bio_part1)
    
    def get_highlighted_bio_part2(self):
        """Get bio part 2 with highlighted keywords"""
        return self.highlight_keywords_in_text(self.bio_part2)
    
    def get_highlighted_bio_hidden1(self):
        """Get hidden bio part 1 with highlighted keywords"""
        return self.highlight_keywords_in_text(self.bio_hidden1)
    
    def get_highlighted_bio_hidden2(self):
        """Get hidden bio part 2 with highlighted keywords"""
        return self.highlight_keywords_in_text(self.bio_hidden2)
    
    def has_more_content(self):
        """Check if advisor has additional content for Read More section"""
        return bool(self.bio_hidden1 or self.bio_hidden2)
    
    



class PlacementsSection(models.Model):
    """Main placements section model"""
    
    # === SECTION HEADER ===
    title = models.CharField(
        max_length=200,
        default='Where Our Students Build Careers',
        help_text="Main title for placements section"
    )
    
    subtitle = models.CharField(
        max_length=300,
        default='Successfully placed across leading tech, finance, and service sector companies.',
        help_text="Subtitle/description below title"
    )
    
    # === STATISTICS ===
    companies_count = models.IntegerField(
        default=50,
        help_text="Number of companies (e.g., 50+)"
    )
    
    students_placed = models.IntegerField(
        default=500,
        help_text="Number of students placed (e.g., 500+)"
    )
    
    sectors_count = models.IntegerField(
        default=10,
        help_text="Number of sectors (e.g., 10+)"
    )
    
    # === DISPLAY SETTINGS ===
    is_active = models.BooleanField(
        default=True,
        help_text="Show this section on placements page"
    )
    
    display_order = models.IntegerField(
        default=1,
        help_text="Order in which sections appear (1 = first)"
    )
    
    # === META INFORMATION ===
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = "Placements Section"
        verbose_name_plural = "Placements Sections"
    
    def __str__(self):
        return f"Placements Section - {self.title}"
    
    @property
    def companies_display(self):
        """Format companies count with + sign"""
        return f"{self.companies_count}+"
    
    @property
    def students_display(self):
        """Format students count with + sign"""
        return f"{self.students_placed}+"
    
    @property
    def sectors_display(self):
        """Format sectors count with + sign"""
        return f"{self.sectors_count}+"


class CompanyLogo(models.Model):
    """Individual company logos for placements section"""
    
    placements_section = models.ForeignKey(
        PlacementsSection,
        on_delete=models.CASCADE,
        related_name='company_logos',
        help_text="Select placements section this logo belongs to"
    )
    
    company_name = models.CharField(
        max_length=100,
        help_text="Company/organization name"
    )
    
    logo = models.ImageField(
        upload_to='placements/company_logos/',
        help_text="Company logo image"
    )
    
    alt_text = models.CharField(
        max_length=100,
        blank=True,
        help_text="Alternative text for accessibility (e.g., 'Infosys Logo')"
    )
    
    display_order = models.IntegerField(
        default=0,
        help_text="Order in which logos appear (0 = first)"
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="Show this company logo"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', 'company_name']
        verbose_name = "Company Logo"
        verbose_name_plural = "Company Logos"
    
    def __str__(self):
        return self.company_name


class ManyMoreCompanies(models.Model):
    """'And Many More' section at the end"""
    
    placements_section = models.ForeignKey(
        PlacementsSection,
        on_delete=models.CASCADE,
        related_name='many_more_section',
        help_text="Select placements section this belongs to"
    )
    
    additional_count = models.IntegerField(
        default=40,
        help_text="Number of additional companies (e.g., 40+)"
    )
    
    label = models.CharField(
        max_length=100,
        default='Leading Companies',
        help_text="Label below the count"
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="Show 'Many More' section"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Many More Companies"
        verbose_name_plural = "Many More Companies Sections"
    
    def __str__(self):
        return f"+{self.additional_count} More Companies"
    
    @property
    def count_display(self):
        """Format additional count with + sign"""
        return f"+{self.additional_count}+"
    
    



from django.db import models


class InternshipSection(models.Model):
    badge_text = models.CharField(
        max_length=100,
        default="Career Launchpad"
    )

    title = models.CharField(max_length=200)

    description = models.TextField(
        max_length=300,
        help_text="Short description shown under title"
    )

    partner_companies = models.PositiveIntegerField(default=300)
    job_conversion_rate = models.PositiveIntegerField(default=85)
    students_placed = models.PositiveIntegerField(default=1200)

    display_order = models.PositiveIntegerField(default=2)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Internship Section"
        verbose_name_plural = "Internship Section"

    def __str__(self):
        return self.title

    @property
    def partner_companies_display(self):
        return f"{self.partner_companies}+"

    @property
    def job_conversion_display(self):
        return f"{self.job_conversion_rate}%"

    @property
    def students_placed_display(self):
        return f"{self.students_placed}+"


class InternshipBenefit(models.Model):

    ICON_CHOICES = [
        ("bi-briefcase", "💼 Real Projects"),
        ("bi-people", "👥 Expert Mentorship"),
        ("bi-award", "🏆 Certification"),
        ("bi-graph-up", "📈 Career Growth"),
        ("bi-building", "🏢 Corporate Exposure"),
        ("bi-lightbulb", "💡 Skill Development"),
    ]

    COLOR_CHOICES = [
        ("primary", "Blue"),
        ("success", "Green"),
        ("warning", "Yellow"),
        ("info", "Light Blue"),
        ("danger", "Red"),
        ("secondary", "Gray"),
    ]

    internship_section = models.ForeignKey(
        InternshipSection,
        on_delete=models.CASCADE,
        related_name="benefits"
    )

    title = models.CharField(max_length=100)

    description = models.CharField(
        max_length=160,
        help_text="Short one-line description"
    )

    icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default="bi-briefcase"
    )

    icon_color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default="primary"
    )

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Internship Benefit"
        verbose_name_plural = "Internship Benefits"

    def __str__(self):
        return self.title

    @property
    def color_class(self):
        return self.icon_color
