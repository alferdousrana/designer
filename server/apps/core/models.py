from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class OrderedModel(models.Model):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ["order", "id"]


from django.db import models

class HeroSection(TimeStampedModel, ActiveModel):
    greeting = models.CharField(
        max_length=100,
        default="Hi, I'm",
        help_text="Small greeting text shown above the hero title."
    )
    full_name = models.CharField(
        max_length=120,
        help_text="Main highlighted name in the hero section."
    )
    profession = models.CharField(
        max_length=200,
        help_text="Second line of hero title, e.g. Product Designer."
    )
    short_bio = models.TextField(
        help_text="Short intro text for homepage hero section."
    )
    profile_image = models.ImageField(
        upload_to="core/hero/",
        blank=True,
        null=True,
        help_text="Profile image shown on the right side of hero section."
    )
    primary_button_text = models.CharField(
        max_length=50,
        default="Get Start",
        help_text="Text for the circular CTA button."
    )
    primary_button_link = models.CharField(
        max_length=255,
        default="#contact",
        help_text="Link for the primary CTA button."
    )

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return f"Hero - {self.full_name}"


class AboutSection(TimeStampedModel, ActiveModel):
    title = models.CharField(max_length=200, default="ABOUT ME")
    subtitle = models.CharField(
        max_length=255,
        blank=True,
        help_text="Main about heading, e.g. Product Designer with 3 Years Of Experience"
    )
    bio = models.TextField()

    profile_image = models.ImageField(upload_to="core/about/", blank=True, null=True)

    hire_me_button_text = models.CharField(max_length=50, default="Hire Me")
    hire_me_button_link = models.CharField(max_length=255, default="#contact")

    download_cv_text = models.CharField(max_length=50, default="Download CV")
    download_cv_link = models.CharField(max_length=255, blank=True, default="#")
    cv_file = models.FileField(upload_to="core/cv/", blank=True, null=True)

    show_play_button = models.BooleanField(default=True)
    video_url = models.URLField(blank=True, null=True)

    awards = models.PositiveIntegerField(default=45)
    completed_projects = models.PositiveIntegerField(default=10)
    years_of_experience = models.PositiveIntegerField(default=3)
    happy_clients = models.PositiveIntegerField(default=16)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.title

class BrandLogo(TimeStampedModel, ActiveModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="core/brands/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Brand Logo"
        verbose_name_plural = "Brand Logos"

    def __str__(self):
        return self.name


class Skill(TimeStampedModel, ActiveModel, OrderedModel):
    title = models.CharField(
        max_length=150,
        help_text="Skill title shown in the skills card, e.g. UI Design.",
    )
    number = models.CharField(
        max_length=10,
        blank=True,
        help_text='Optional custom display number, e.g. "01.". Leave blank to generate from order in frontend.',
    )
    description = models.TextField(
        blank=True,
        help_text="Short description shown under the skill title.",
    )
    project_link = models.CharField(
        max_length=255,
        blank=True,
        default="#",
        help_text="Link for the skill action button, e.g. portfolio/project section URL.",
    )
    project_link_text = models.CharField(
        max_length=50,
        default="See Past Work",
        help_text="Button/link text shown at the bottom of the skill card.",
    )

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.title



class ExperienceSection(TimeStampedModel, ActiveModel):
    eyebrow = models.CharField(
        max_length=150,
        default="MY JOURNEY & TRACK RECORD",
        help_text="Small heading text shown above the main experience title.",
    )
    title_light = models.CharField(
        max_length=100,
        default="Tons Of",
        help_text="First/light part of the main experience heading.",
    )
    title_accent = models.CharField(
        max_length=100,
        default="Experiences",
        help_text="Second/accent part of the main experience heading.",
    )
    experience_image = models.ImageField(
        upload_to="core/experience/",
        blank=True,
        null=True,
        help_text="Main image shown on the left side of the experience section.",
    )

    class Meta:
        verbose_name = "Experience Section"
        verbose_name_plural = "Experience Section"

    def __str__(self):
        return "Experience Section"


class ExperienceItem(TimeStampedModel, ActiveModel, OrderedModel):
    year = models.CharField(
        max_length=20,
        help_text='Year or label shown in the small badge, e.g. "2022".',
    )
    title = models.CharField(
        max_length=150,
        help_text="Experience item title, e.g. Product Manager.",
    )
    description = models.TextField(
        blank=True,
        help_text="Short description shown under the experience item title.",
    )

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Experience Item"
        verbose_name_plural = "Experience Items"

    def __str__(self):
        return f"{self.year} - {self.title}"





class TestimonialsSection(TimeStampedModel, ActiveModel):
    title_light = models.CharField(
        max_length=100,
        default="Clients",
        help_text="First/light part of the testimonials section heading.",
    )
    title_accent = models.CharField(
        max_length=100,
        default="Talking",
        help_text="Second/accent part of the testimonials section heading.",
    )
    satisfaction_rate = models.CharField(
        max_length=20,
        default="100%",
        help_text='Satisfaction metric shown on the right side, e.g. "100%".',
    )
    satisfaction_rate_label = models.CharField(
        max_length=100,
        default="Satisfaction Rate",
        help_text="Label for the satisfaction metric.",
    )
    repeat_order_rate = models.CharField(
        max_length=20,
        default="97%",
        help_text='Repeat order metric shown on the right side, e.g. "97%".',
    )
    repeat_order_label = models.CharField(
        max_length=100,
        default="Repeat Order",
        help_text="Label for the repeat order metric.",
    )
    google_review_rating = models.CharField(
        max_length=20,
        default="4.8",
        help_text='Google review rating shown on the right side, e.g. "4.8".',
    )
    google_review_label = models.CharField(
        max_length=100,
        default="Google Review",
        help_text="Label for the Google review metric.",
    )
    hire_button_text = models.CharField(
        max_length=50,
        default="Hire Me",
        help_text="Text for the CTA button in the testimonials section.",
    )
    hire_button_link = models.CharField(
        max_length=255,
        default="#contact",
        help_text="Link for the CTA button in the testimonials section.",
    )

    class Meta:
        verbose_name = "Testimonials Section"
        verbose_name_plural = "Testimonials Section"

    def __str__(self):
        return "Testimonials Section"


class Testimonial(TimeStampedModel, ActiveModel, OrderedModel):
    client_name = models.CharField(
        max_length=120,
        help_text="Client name shown in the testimonial card.",
    )
    client_role = models.CharField(
        max_length=150,
        blank=True,
        help_text="Client role/designation shown under the client name.",
    )
    client_company = models.CharField(
        max_length=150,
        blank=True,
        help_text="Optional client company name shown after the role.",
    )
    client_photo = models.ImageField(
        upload_to="core/testimonials/",
        blank=True,
        null=True,
        help_text="Client photo shown in the testimonial card.",
    )
    review = models.TextField(
        help_text="Testimonial/review text shown in the card.",
    )
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Client rating value from 1 to 5.",
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Mark as featured testimonial if needed for frontend filtering later.",
    )

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        company = f" - {self.client_company}" if self.client_company else ""
        return f"{self.client_name}{company}"


class ProjectsShowcaseSection(TimeStampedModel, ActiveModel):
    eyebrow = models.CharField(
        max_length=100,
        default="SHOW CASE",
        help_text="Small text shown above the main heading.",
    )
    title_light = models.CharField(
        max_length=100,
        default="Discover",
        help_text="First/light part of the section title.",
    )
    title_accent = models.CharField(
        max_length=100,
        default="How I Work",
        help_text="Second/accent part of the section title.",
    )
    max_items = models.PositiveIntegerField(
        default=6,
        help_text="Maximum number of featured projects to display in this section.",
    )

    class Meta:
        verbose_name = "Projects Showcase Section"
        verbose_name_plural = "Projects Showcase Section"

    def __str__(self):
        return "Projects Showcase Section"
    

class BlogSection(TimeStampedModel, ActiveModel):
    eyebrow = models.CharField(
        max_length=100,
        default="LATEST ARTICLES",
        help_text="Small text shown above the main blog section heading.",
    )
    title_light = models.CharField(
        max_length=100,
        default="My Blog",
        help_text="First/light part of the blog section title.",
    )
    title_accent = models.CharField(
        max_length=100,
        default="For You",
        help_text="Second/accent part of the blog section title.",
    )
    max_items = models.PositiveIntegerField(
        default=3,
        help_text="Maximum number of featured blog posts to show in this section.",
    )

    class Meta:
        verbose_name = "Blog Section"
        verbose_name_plural = "Blog Section"

    def __str__(self):
        return "Blog Section"
    

class SocialPlatform(models.TextChoices):
    DRIBBBLE = "dribbble", "Dribbble"
    FACEBOOK = "facebook", "Fb"
    INSTAGRAM = "instagram", "Ig"
    BEHANCE = "behance", "Be"
    LINKEDIN = "linkedin", "In"
    YOUTUBE = "youtube", "Ytb"
    TWITTER = "twitter", "Twitter"
    GITHUB = "github", "GitHub"


class ContactSection(TimeStampedModel, ActiveModel):
    eyebrow = models.CharField(
        max_length=100,
        default="INTERESTED?",
        help_text="Small text shown above the main contact heading.",
    )
    title_light = models.CharField(
        max_length=100,
        default="Let's",
        help_text="First/light part of the contact section title.",
    )
    title_accent = models.CharField(
        max_length=100,
        default="Connect!",
        help_text="Second/accent part of the contact section title.",
    )
    submit_button_text = models.CharField(
        max_length=50,
        default="Send",
        help_text="Text shown on the contact form submit button.",
    )
    footer_logo_text = models.CharField(
        max_length=50,
        default="RiJU",
        help_text="Footer logo/brand text shown in the bottom bar.",
    )
    footer_copyright_text = models.CharField(
        max_length=100,
        default="© 2026 Riju",
        help_text="Footer copyright text shown beside the footer logo.",
    )
    footer_credit_text = models.CharField(
        max_length=100,
        default="by Afroza Riju",
        help_text="Footer credit text shown in the bottom bar.",
    )

    class Meta:
        verbose_name = "Contact Section"
        verbose_name_plural = "Contact Section"

    def __str__(self):
        return "Contact Section"


class SocialLink(TimeStampedModel, ActiveModel, OrderedModel):
    platform = models.CharField(
        max_length=50,
        choices=SocialPlatform.choices,
        help_text="Social platform name shown in the footer social links.",
    )
    url = models.URLField(
        help_text="Full social profile URL.",
    )

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"

    def __str__(self):
        return self.get_platform_display()

    @property
    def platform_display(self):
        return self.get_platform_display()

    @property
    def icon_class(self):
        ICON_MAP = {
            "dribbble": "fa-brands fa-dribbble",
            "facebook": "fa-brands fa-facebook-f",
            "instagram": "fa-brands fa-instagram",
            "behance": "fa-brands fa-behance",
            "linkedin": "fa-brands fa-linkedin-in",
            "youtube": "fa-brands fa-youtube",
            "twitter": "fa-brands fa-x-twitter",
            "github": "fa-brands fa-github",
        }
        return ICON_MAP.get(self.platform, "")


class ContactInfo(TimeStampedModel, ActiveModel):
    email = models.EmailField(
        help_text="Primary contact email shown on the left side of the section.",
    )
    phone = models.CharField(
        max_length=30,
        blank=True,
        help_text="Primary phone number shown on the left side of the section.",
    )
    whatsapp = models.CharField(
        max_length=30,
        blank=True,
        help_text="Optional WhatsApp number for contact purposes.",
    )
    location = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional location text if needed later.",
    )
    availability_text = models.TextField(
        blank=True,
        help_text="Main descriptive text shown under the contact heading.",
    )

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.email


class ContactMessageStatus(models.TextChoices):
    NEW = "new", "New"
    IN_PROGRESS = "in_progress", "In Progress"
    REPLIED = "replied", "Replied"
    CLOSED = "closed", "Closed"


class ContactMessage(TimeStampedModel):
    full_name = models.CharField(
        max_length=120,
        blank=True,
        help_text="Sender full name from the contact form.",
    )
    email = models.EmailField(
        help_text="Sender email address.",
    )
    subject = models.CharField(
        max_length=200,
        help_text="Generated or custom subject for the contact message.",
    )
    message = models.TextField(
        help_text="Main message content from the contact form.",
    )
    phone = models.CharField(
        max_length=30,
        blank=True,
        help_text="Sender phone number.",
    )
    company_name = models.CharField(
        max_length=150,
        blank=True,
        help_text="Optional company name.",
    )
    budget = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional project budget.",
    )
    project_type = models.CharField(
        max_length=100,
        blank=True,
        help_text="Selected service/interest type from the contact form.",
    )
    status = models.CharField(
        max_length=20,
        choices=ContactMessageStatus.choices,
        default=ContactMessageStatus.NEW,
        help_text="Admin workflow status of the contact message.",
    )
    is_read = models.BooleanField(
        default=False,
        help_text="Marks whether the message has been read by admin.",
    )
    replied_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Date and time when the message was replied to.",
    )
    admin_note = models.TextField(
        blank=True,
        help_text="Internal admin note for this contact message.",
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.full_name or self.email} - {self.subject}"