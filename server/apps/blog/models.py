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


class BlogCategory(TimeStampedModel, ActiveModel, OrderedModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogTag(TimeStampedModel, ActiveModel, OrderedModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=70, unique=True, blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Blog Tag"
        verbose_name_plural = "Blog Tags"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogPost(TimeStampedModel, ActiveModel, OrderedModel):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True, blank=True)

    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
    )
    tags = models.ManyToManyField(
        BlogTag,
        blank=True,
        related_name="posts",
    )

    excerpt = models.CharField(
        max_length=320,
        blank=True,
        help_text="Short summary for blog cards and previews.",
    )
    content = CKEditor5Field("Content", config_name="default", blank=True)

    featured_image = models.ImageField(upload_to="blog/featured/", blank=True, null=True)
    cover_image = models.ImageField(upload_to="blog/covers/", blank=True, null=True)

    author_name = models.CharField(max_length=120, blank=True, default="Admin")

    read_time = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text="Estimated reading time in minutes.",
    )
    view_count = models.PositiveIntegerField(default=0)

    keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated keywords for search and SEO.",
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
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_keywords_list(self):
        return [keyword.strip() for keyword in self.keywords.split(",") if keyword.strip()]

    def __str__(self):
        return self.title


class BlogImage(TimeStampedModel, ActiveModel, OrderedModel):
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name="gallery",
    )
    image = models.ImageField(upload_to="blog/gallery/")
    caption = models.CharField(max_length=200, blank=True)
    alt_text = models.CharField(max_length=255, blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Blog Image"
        verbose_name_plural = "Blog Images"

    def __str__(self):
        return f"{self.post.title} - Image {self.order}"


class BlogSection(TimeStampedModel, ActiveModel, OrderedModel):
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name="sections",
    )
    title = models.CharField(max_length=200, blank=True)
    content = CKEditor5Field("Content", config_name="default", blank=True)
    image = models.ImageField(upload_to="blog/sections/", blank=True, null=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Blog Section"
        verbose_name_plural = "Blog Sections"

    def __str__(self):
        return f"{self.post.title} - {self.title}"