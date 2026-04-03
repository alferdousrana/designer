from django.contrib import admin
from .models import (
    Category,
    ProjectTag,
    Project,
    ProjectImage,
    ProjectSection,
    ProjectMetric,
)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ("image", "caption", "alt_text", "order", "is_active")
    ordering = ("order",)
    show_change_link = True


class ProjectSectionInline(admin.StackedInline):
    model = ProjectSection
    extra = 1
    fields = ("title", "content", "image", "order", "is_active")
    ordering = ("order",)
    show_change_link = True


class ProjectMetricInline(admin.TabularInline):
    model = ProjectMetric
    extra = 1
    fields = ("label", "value", "order", "is_active")
    ordering = ("order",)
    show_change_link = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "slug", "description")
    list_editable = ("order", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")
    ordering = ("order", "-created_at")

    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "slug", "description")
        }),
        ("Status & Order", {
            "fields": ("order", "is_active")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
    )


@admin.register(ProjectTag)
class ProjectTagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "slug")
    list_editable = ("order", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")
    ordering = ("order", "-created_at")

    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "slug")
        }),
        ("Status & Order", {
            "fields": ("order", "is_active")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "status",
        "is_featured",
        "is_highlighted",
        "is_active",
        "view_count",
        "read_time",
        "order",
        "created_at",
    )
    list_filter = (
        "status",
        "is_featured",
        "is_highlighted",
        "is_active",
        "category",
        "created_at",
    )
    search_fields = (
        "title",
        "slug",
        "short_desc",
        "overview",
        "tools_used",
        "my_role",
        "keywords",
        "seo_title",
        "seo_description",
    )
    list_editable = (
        "status",
        "is_featured",
        "is_highlighted",
        "is_active",
        "order",
    )
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    readonly_fields = ("created_at", "updated_at", "view_count")
    ordering = ("order", "-created_at")
    inlines = [ProjectImageInline, ProjectSectionInline, ProjectMetricInline]

    fieldsets = (
        ("Basic Info", {
            "fields": (
                "title",
                "slug",
                "category",
                "tags",
                "short_desc",
                "overview",
            )
        }),
        ("Images", {
            "fields": (
                "thumbnail",
                "cover_image",
            )
        }),
        ("Project Details", {
            "fields": (
                "tools_used",
                "my_role",
                "duration",
            )
        }),
        ("Links", {
            "fields": (
                "live_url",
                "behance_url",
                "github_url",
                "figma_url",
            )
        }),
        ("Performance & Search", {
            "fields": (
                "read_time",
                "view_count",
                "keywords",
            )
        }),
        ("Publishing", {
            "fields": (
                "status",
                "published_at",
                "is_featured",
                "is_highlighted",
                "is_active",
                "order",
            )
        }),
        ("SEO", {
            "fields": (
                "seo_title",
                "seo_description",
            )
        }),
        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )