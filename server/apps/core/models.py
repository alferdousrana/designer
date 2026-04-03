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


class HeroSection(TimeStampedModel, ActiveModel):
    greeting = models.CharField(max_length=100, default="Hi, I'm")
    full_name = models.CharField(max_length=120)
    profession = models.CharField(max_length=200)
    short_bio = models.TextField(help_text="Short intro text for homepage hero section.")
    primary_button_text = models.CharField(max_length=50, default="View My Work")
    primary_button_link = models.CharField(max_length=255, default="#projects")
    secondary_button_text = models.CharField(max_length=50, blank=True, default="Download Resume")
    secondary_button_link = models.CharField(max_length=255, blank=True)
    resume_file = models.FileField(upload_to="core/resume/", blank=True, null=True)
    profile_image = models.ImageField(upload_to="core/hero/", blank=True, null=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return f"Hero - {self.full_name}"


class AboutSection(TimeStampedModel, ActiveModel):
    title = models.CharField(max_length=200, default="About Me")
    subtitle = models.CharField(max_length=255, blank=True)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to="core/about/", blank=True, null=True)

    years_of_experience = models.PositiveIntegerField(default=0)
    completed_projects = models.PositiveIntegerField(default=0)
    happy_clients = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.title


class SkillCategory(models.TextChoices):
    DESIGN = "design", "Design"
    TOOL = "tool", "Tool"
    RESEARCH = "research", "Research"
    DEVELOPMENT = "development", "Development"
    OTHER = "other", "Other"


class Skill(TimeStampedModel, ActiveModel, OrderedModel):
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=SkillCategory.choices,
        default=SkillCategory.DESIGN,
    )
    icon_image = models.ImageField(upload_to="core/skills/", blank=True, null=True)
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional icon class for frontend icon libraries.",
    )
    proficiency = models.PositiveSmallIntegerField(
        default=80,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Skill level in percentage.",
    )

    def __str__(self):
        return self.name


class Service(TimeStampedModel, ActiveModel, OrderedModel):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    icon_class = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class Testimonial(TimeStampedModel, ActiveModel, OrderedModel):
    client_name = models.CharField(max_length=120)
    client_role = models.CharField(max_length=150, blank=True)
    client_company = models.CharField(max_length=150, blank=True)
    client_photo = models.ImageField(upload_to="core/testimonials/", blank=True, null=True)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    is_featured = models.BooleanField(default=False)

    class Meta(OrderedModel.Meta):
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        company = f" - {self.client_company}" if self.client_company else ""
        return f"{self.client_name}{company}"


class SocialPlatform(models.TextChoices):
    LINKEDIN = "linkedin", "LinkedIn"
    BEHANCE = "behance", "Behance"
    DRIBBBLE = "dribbble", "Dribbble"
    GITHUB = "github", "GitHub"
    TWITTER = "twitter", "Twitter"
    FACEBOOK = "facebook", "Facebook"
    INSTAGRAM = "instagram", "Instagram"


class SocialLink(TimeStampedModel, ActiveModel, OrderedModel):
    platform = models.CharField(
        max_length=50,
        choices=SocialPlatform.choices,
    )
    url = models.URLField()

    class Meta(OrderedModel.Meta):
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"

    def __str__(self):
        return self.get_platform_display()

    @property
    def icon_class(self):
        ICON_MAP = {
            "linkedin": "fa-brands fa-linkedin",
            "behance": "fa-brands fa-behance",
            "dribbble": "fa-brands fa-dribbble",
            "github": "fa-brands fa-github",
            "twitter": "fa-brands fa-x-twitter",
            "facebook": "fa-brands fa-facebook",
            "instagram": "fa-brands fa-instagram",
        }
        return ICON_MAP.get(self.platform, "")


class ContactInfo(TimeStampedModel, ActiveModel):
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    whatsapp = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=200, blank=True)
    availability_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Example: Available for freelance and full-time roles.",
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
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    phone = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=150, blank=True)
    budget = models.CharField(max_length=100, blank=True)
    project_type = models.CharField(max_length=100, blank=True)

    status = models.CharField(
        max_length=20,
        choices=ContactMessageStatus.choices,
        default=ContactMessageStatus.NEW,
    )
    is_read = models.BooleanField(default=False)
    replied_at = models.DateTimeField(blank=True, null=True)
    admin_note = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.full_name} - {self.subject}"