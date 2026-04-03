from django.contrib import admin
from .models import (
    HeroSection,
    AboutSection,
    Skill,
    Service,
    Testimonial,
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
    search_fields = ("full_name", "profession")
    fieldsets = (
        ("Basic Info", {
            "fields": ("greeting", "full_name", "profession", "short_bio")
        }),
        ("Buttons", {
            "fields": (
                "primary_button_text",
                "primary_button_link",
                "secondary_button_text",
                "secondary_button_link",
            )
        }),
        ("Media", {
            "fields": ("resume_file", "profile_image")
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
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("title", "subtitle")
    fieldsets = (
        ("Content", {
            "fields": ("title", "subtitle", "bio", "profile_image")
        }),
        ("Stats", {
            "fields": (
                "years_of_experience",
                "completed_projects",
                "happy_clients",
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
    search_fields = ("email", "phone", "location", "availability_text")
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


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "proficiency",
        "order",
        "is_active",
    )
    list_filter = ("category", "is_active")
    search_fields = ("name",)
    list_editable = ("order", "proficiency", "is_active")
    ordering = ("order", "id")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "order",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active",)
    search_fields = ("title", "short_description", "slug")
    list_editable = ("order", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order", "id")


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
        "company_name",
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