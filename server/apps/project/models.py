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


class Category(TimeStampedModel, ActiveModel, OrderedModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProjectTag(TimeStampedModel, ActiveModel, OrderedModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=70, unique=True, blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Project Tag"
        verbose_name_plural = "Project Tags"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(TimeStampedModel, ActiveModel, OrderedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="projects",
    )
    tags = models.ManyToManyField(
        ProjectTag,
        blank=True,
        related_name="projects",
    )

    short_desc = models.CharField(max_length=300, blank=True)
    overview = CKEditor5Field('Content', config_name='default', blank=True)

    thumbnail = models.ImageField(upload_to="projects/thumbnails/", blank=True, null=True)
    cover_image = models.ImageField(upload_to="projects/covers/", blank=True, null=True)

    tools_used = models.CharField(
        max_length=300,
        blank=True,
        help_text="Comma-separated: Figma, Miro, Notion",
    )
    my_role = models.CharField(max_length=200, blank=True)
    duration = models.CharField(
        max_length=100,
        blank=True,
        help_text='Example: "3 Months"',
    )

    live_url = models.URLField(blank=True)
    behance_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
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
        verbose_name = "Project"
        verbose_name_plural = "Projects"

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


class ProjectImage(TimeStampedModel, ActiveModel, OrderedModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="gallery",
    )
    image = models.ImageField(upload_to="projects/gallery/")
    caption = models.CharField(max_length=200, blank=True)
    alt_text = models.CharField(max_length=255, blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"


class ProjectSection(TimeStampedModel, ActiveModel, OrderedModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="sections",
    )
    title = models.CharField(max_length=200, blank=True)
    content = CKEditor5Field('Content', config_name='default', blank=True)
    image = models.ImageField(upload_to="projects/sections/", blank=True, null=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Project Section"
        verbose_name_plural = "Project Sections"

    def __str__(self):
        return f"{self.project.title} - {self.title}"


class ProjectMetric(TimeStampedModel, ActiveModel, OrderedModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="metrics",
    )
    label = models.CharField(max_length=100,)
    value = models.CharField(max_length=100, help_text="Example: 40%, 12K+, 3 Weeks", blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Project Metric"
        verbose_name_plural = "Project Metrics"

    def __str__(self):
        return f"{self.project.title} - {self.label}"