from django.contrib import admin
from .models import (
    BlogCategory,
    BlogTag,
    BlogPost,
    BlogImage,
    BlogSection,
)


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1
    fields = ("image", "caption", "alt_text", "order", "is_active")
    ordering = ("order",)
    show_change_link = True


class BlogSectionInline(admin.StackedInline):
    model = BlogSection
    extra = 1
    fields = ("title", "content", "image", "order", "is_active")
    ordering = ("order",)
    show_change_link = True


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
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


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
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


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "author_name",
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
        "excerpt",
        "content",
        "author_name",
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
    inlines = [BlogImageInline, BlogSectionInline]

    fieldsets = (
        ("Basic Info", {
            "fields": (
                "title",
                "slug",
                "category",
                "tags",
                "author_name",
                "excerpt",
                "content",
            )
        }),
        ("Images", {
            "fields": (
                "featured_image",
                "cover_image",
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