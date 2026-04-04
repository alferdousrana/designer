from django.contrib import admin
from .models import (
    HeroSection,
    AboutSection,
    BrandLogo,
    Skill,
    ExperienceSection,
    ExperienceItem,
    TestimonialsSection,
    Testimonial,
    ProjectsShowcaseSection,
    BlogSection,
    ContactSection,
    SocialLink,
    ContactInfo,
    ContactMessage,
)


class SingleInstanceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()


@admin.register(HeroSection)
class HeroSectionAdmin(SingleInstanceAdmin):
    list_display = (
        "full_name",
        "profession",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("full_name", "profession", "greeting", "short_bio")
    fieldsets = (
        ("Basic Info", {
            "fields": ("greeting", "full_name", "profession", "short_bio")
        }),
        ("CTA Button", {
            "fields": ("primary_button_text", "primary_button_link")
        }),
        ("Media", {
            "fields": ("profile_image",)
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
    )


@admin.register(AboutSection)
class AboutSectionAdmin(SingleInstanceAdmin):
    list_display = (
        "title",
        "years_of_experience",
        "completed_projects",
        "happy_clients",
        "awards",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("title", "subtitle", "bio")
    fieldsets = (
        ("Content", {
            "fields": ("title", "subtitle", "bio", "profile_image")
        }),
        ("Buttons & Media", {
            "fields": (
                "hire_me_button_text",
                "hire_me_button_link",
                "download_cv_text",
                "download_cv_link",
                "cv_file",
                "show_play_button",
                "video_url",
            )
        }),
        ("Stats", {
            "fields": (
                "awards",
                "completed_projects",
                "years_of_experience",
                "happy_clients",
            )
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
    )


@admin.register(BrandLogo)
class BrandLogoAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "order",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)
    list_editable = ("order", "is_active")
    ordering = ("order", "id")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "number",
        "project_link_text",
        "order",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("title", "description", "number")
    list_editable = ("order", "is_active")
    ordering = ("order", "id")


@admin.register(ExperienceSection)
class ExperienceSectionAdmin(SingleInstanceAdmin):
    list_display = (
        "title_light",
        "title_accent",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("eyebrow", "title_light", "title_accent")
    fieldsets = (
        ("Heading", {
            "fields": ("eyebrow", "title_light", "title_accent")
        }),
        ("Media", {
            "fields": ("experience_image",)
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
    )


@admin.register(ExperienceItem)
class ExperienceItemAdmin(admin.ModelAdmin):
    list_display = (
        "year",
        "title",
        "order",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("year", "title", "description")
    list_editable = ("order", "is_active")
    ordering = ("order", "id")


@admin.register(TestimonialsSection)
class TestimonialsSectionAdmin(SingleInstanceAdmin):
    list_display = (
        "title_light",
        "title_accent",
        "satisfaction_rate",
        "repeat_order_rate",
        "google_review_rating",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = (
        "title_light",
        "title_accent",
        "satisfaction_rate_label",
        "repeat_order_label",
        "google_review_label",
    )
    fieldsets = (
        ("Heading", {
            "fields": ("title_light", "title_accent")
        }),
        ("Metrics", {
            "fields": (
                "satisfaction_rate",
                "satisfaction_rate_label",
                "repeat_order_rate",
                "repeat_order_label",
                "google_review_rating",
                "google_review_label",
            )
        }),
        ("CTA Button", {
            "fields": ("hire_button_text", "hire_button_link")
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "client_name",
        "client_company",
        "rating",
        "is_featured",
        "order",
        "is_active",
        "created_at",
    )
    list_filter = ("is_featured", "is_active", "rating")
    search_fields = ("client_name", "client_company", "client_role", "review")
    list_editable = ("rating", "is_featured", "order", "is_active")
    ordering = ("order", "id")


@admin.register(ProjectsShowcaseSection)
class ProjectsShowcaseSectionAdmin(SingleInstanceAdmin):
    list_display = (
        "title_light",
        "title_accent",
        "max_items",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("eyebrow", "title_light", "title_accent")
    fieldsets = (
        ("Heading", {
            "fields": ("eyebrow", "title_light", "title_accent")
        }),
        ("Display Settings", {
            "fields": ("max_items",)
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
    )


@admin.register(BlogSection)
class BlogSectionAdmin(SingleInstanceAdmin):
    list_display = (
        "title_light",
        "title_accent",
        "max_items",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("eyebrow", "title_light", "title_accent")
    fieldsets = (
        ("Heading", {
            "fields": ("eyebrow", "title_light", "title_accent")
        }),
        ("Display Settings", {
            "fields": ("max_items",)
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
    )


@admin.register(ContactSection)
class ContactSectionAdmin(SingleInstanceAdmin):
    list_display = (
        "title_light",
        "title_accent",
        "submit_button_text",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = (
        "eyebrow",
        "title_light",
        "title_accent",
        "footer_logo_text",
        "footer_copyright_text",
        "footer_credit_text",
    )
    fieldsets = (
        ("Heading", {
            "fields": ("eyebrow", "title_light", "title_accent")
        }),
        ("Form Button", {
            "fields": ("submit_button_text",)
        }),
        ("Footer", {
            "fields": (
                "footer_logo_text",
                "footer_copyright_text",
                "footer_credit_text",
            )
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(SingleInstanceAdmin):
    list_display = (
        "email",
        "phone",
        "whatsapp",
        "location",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("email", "phone", "whatsapp", "location", "availability_text")
    fieldsets = (
        ("Contact Details", {
            "fields": (
                "email",
                "phone",
                "whatsapp",
                "location",
                "availability_text",
            )
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
    )


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = (
        "platform",
        "url",
        "order",
        "is_active",
        "updated_at",
    )
    list_filter = ("platform", "is_active")
    search_fields = ("platform", "url")
    list_editable = ("order", "is_active")
    ordering = ("order", "id")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "subject",
        "project_type",
        "status",
        "is_read",
        "created_at",
    )
    list_filter = ("status", "is_read", "created_at")
    search_fields = (
        "full_name",
        "email",
        "subject",
        "message",
        "phone",
        "company_name",
        "budget",
        "project_type",
    )
    list_editable = ("status", "is_read")
    readonly_fields = ("created_at", "updated_at", "replied_at")
    fieldsets = (
        ("Sender Info", {
            "fields": ("full_name", "email", "phone", "company_name")
        }),
        ("Project Info", {
            "fields": ("subject", "project_type", "budget", "message")
        }),
        ("Admin Management", {
            "fields": ("status", "is_read", "replied_at", "admin_note")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
    )