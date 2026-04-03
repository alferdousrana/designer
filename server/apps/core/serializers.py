from rest_framework import serializers
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


class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = [
            "id",
            "greeting",
            "full_name",
            "profession",
            "short_bio",
            "primary_button_text",
            "primary_button_link",
            "secondary_button_text",
            "secondary_button_link",
            "resume_file",
            "profile_image",
            "is_active",
        ]


class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = [
            "id",
            "title",
            "subtitle",
            "bio",
            "profile_image",
            "years_of_experience",
            "completed_projects",
            "happy_clients",
            "is_active",
        ]


class SkillSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source="get_category_display", read_only=True)

    class Meta:
        model = Skill
        fields = [
            "id",
            "name",
            "category",
            "category_display",
            "icon_image",
            "icon_class",
            "proficiency",
            "order",
            "is_active",
        ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "short_description",
            "icon_class",
            "slug",
            "order",
            "is_active",
        ]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            "id",
            "client_name",
            "client_role",
            "client_company",
            "client_photo",
            "review",
            "rating",
            "is_featured",
            "order",
            "is_active",
        ]


class SocialLinkSerializer(serializers.ModelSerializer):
    platform_display = serializers.CharField(source="get_platform_display", read_only=True)
    icon_class = serializers.ReadOnlyField()

    class Meta:
        model = SocialLink
        fields = [
            "id",
            "platform",
            "platform_display",
            "url",
            "icon_class",
            "order",
            "is_active",
        ]


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = [
            "id",
            "email",
            "phone",
            "whatsapp",
            "location",
            "availability_text",
            "is_active",
        ]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            "id",
            "full_name",
            "email",
            "subject",
            "message",
            "phone",
            "company_name",
            "budget",
            "project_type",
        ]


class ContactMessageAdminSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = ContactMessage
        fields = [
            "id",
            "full_name",
            "email",
            "subject",
            "message",
            "phone",
            "company_name",
            "budget",
            "project_type",
            "status",
            "status_display",
            "is_read",
            "replied_at",
            "admin_note",
            "created_at",
            "updated_at",
        ]


class HomePageSerializer(serializers.Serializer):
    hero = HeroSectionSerializer(allow_null=True)
    about = AboutSectionSerializer(allow_null=True)
    skills = SkillSerializer(many=True)
    services = ServiceSerializer(many=True)
    testimonials = TestimonialSerializer(many=True)
    social_links = SocialLinkSerializer(many=True)
    contact_info = ContactInfoSerializer(allow_null=True)