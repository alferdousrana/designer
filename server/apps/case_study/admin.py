from django.contrib import admin
from .models import (
    CaseStudy,
    CaseStudyImage,
    CaseStudySection,
    CaseStudyMetric,
)


class CaseStudyImageInline(admin.TabularInline):
    model = CaseStudyImage
    extra = 1
    fields = ("image", "caption", "alt_text", "order", "is_active")
    ordering = ("order",)
    show_change_link = True


class CaseStudySectionInline(admin.StackedInline):
    model = CaseStudySection
    extra = 1
    fields = ("title", "content", "image", "order", "is_active")
    ordering = ("order",)
    show_change_link = True


class CaseStudyMetricInline(admin.TabularInline):
    model = CaseStudyMetric
    extra = 1
    fields = ("label", "value", "order", "is_active")
    ordering = ("order",)
    show_change_link = True


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project_name",
        "client_name",
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
        "created_at",
    )
    search_fields = (
        "title",
        "slug",
        "project_name",
        "client_name",
        "industry",
        "short_desc",
        "overview",
        "my_role",
        "team",
        "timeline",
        "tools_used",
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
    readonly_fields = ("created_at", "updated_at", "view_count")
    ordering = ("order", "-created_at")
    inlines = [CaseStudyImageInline, CaseStudySectionInline, CaseStudyMetricInline]

    fieldsets = (
        ("Basic Info", {
            "fields": (
                "title",
                "slug",
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
        ("Project Context", {
            "fields": (
                "project_name",
                "client_name",
                "industry",
                "my_role",
                "team",
                "timeline",
                "tools_used",
            )
        }),
        ("Core Case Study Content", {
            "fields": (
                "challenge",
                "goal",
                "process",
                "solution",
                "outcome",
            )
        }),
        ("Links", {
            "fields": (
                "live_url",
                "prototype_url",
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