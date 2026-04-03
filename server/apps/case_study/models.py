from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from django_ckeditor_5.fields import CKEditor5Field


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
        ordering = ["order", "-created_at"]


class PublishStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"
    ARCHIVED = "archived", "Archived"


class CaseStudy(TimeStampedModel, ActiveModel, OrderedModel):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True, blank=True)

    short_desc = models.CharField(max_length=320, blank=True)
    overview = CKEditor5Field("Content", config_name="default", blank=True)

    thumbnail = models.ImageField(upload_to="case_study/thumbnails/", blank=True, null=True)
    cover_image = models.ImageField(upload_to="case_study/covers/", blank=True, null=True)

    project_name = models.CharField(max_length=200, blank=True)
    client_name = models.CharField(max_length=200, blank=True)
    industry = models.CharField(max_length=150, blank=True)

    my_role = models.CharField(max_length=200, blank=True)
    team = models.CharField(max_length=255, blank=True)
    timeline = models.CharField(max_length=120, blank=True)

    tools_used = models.CharField(
        max_length=300,
        blank=True,
        help_text="Comma-separated: Figma, Miro, Notion",
    )

    challenge = CKEditor5Field("challenge", config_name="default", blank=True)
    goal = CKEditor5Field("goal", config_name="default", blank=True)
    process = CKEditor5Field("process", config_name="default", blank=True)
    solution = CKEditor5Field("solution", config_name="default", blank=True)
    outcome = CKEditor5Field("outcome", config_name="default", blank=True)

    live_url = models.URLField(blank=True)
    prototype_url = models.URLField(blank=True)
    figma_url = models.URLField(blank=True)

    read_time = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text="Estimated reading time in minutes.",
    )
    view_count = models.PositiveIntegerField(default=0)

    keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated keywords for SEO/search.",
    )

    is_featured = models.BooleanField(default=False)
    is_highlighted = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT,
    )
    published_at = models.DateTimeField(blank=True, null=True)

    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Case Study"
        verbose_name_plural = "Case Studies"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_tools_list(self):
        return [tool.strip() for tool in self.tools_used.split(",") if tool.strip()]

    def get_keywords_list(self):
        return [keyword.strip() for keyword in self.keywords.split(",") if keyword.strip()]

    def __str__(self):
        return self.title


class CaseStudyImage(TimeStampedModel, ActiveModel, OrderedModel):
    case_study = models.ForeignKey(
        CaseStudy,
        on_delete=models.CASCADE,
        related_name="gallery",
    )
    image = models.ImageField(upload_to="case_study/gallery/")
    caption = models.CharField(max_length=200, blank=True)
    alt_text = models.CharField(max_length=255, blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Case Study Image"
        verbose_name_plural = "Case Study Images"

    def __str__(self):
        return f"{self.case_study.title} - Image {self.order}"


class CaseStudySection(TimeStampedModel, ActiveModel, OrderedModel):
    case_study = models.ForeignKey(
        CaseStudy,
        on_delete=models.CASCADE,
        related_name="sections",
    )
    title = models.CharField(max_length=200, blank=True)
    content = CKEditor5Field("Content", config_name="default", blank=True)
    image = models.ImageField(upload_to="case_study/sections/", blank=True, null=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Case Study Section"
        verbose_name_plural = "Case Study Sections"

    def __str__(self):
        return f"{self.case_study.title} - {self.title}"


class CaseStudyMetric(TimeStampedModel, ActiveModel, OrderedModel):
    case_study = models.ForeignKey(
        CaseStudy,
        on_delete=models.CASCADE,
        related_name="metrics",
    )
    label = models.CharField(max_length=100)
    value = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: 40%, 12 interviews, 3 weeks",
    )

    class Meta(OrderedModel.Meta):
        verbose_name = "Case Study Metric"
        verbose_name_plural = "Case Study Metrics"

    def __str__(self):
        return f"{self.case_study.title} - {self.label}"