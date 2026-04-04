from rest_framework import serializers
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
            "hire_me_button_text",
            "hire_me_button_link",
            "download_cv_text",
            "download_cv_link",
            "cv_file",
            "show_play_button",
            "video_url",
            "awards",
            "completed_projects",
            "years_of_experience",
            "happy_clients",
            "is_active",
        ]


class BrandLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandLogo
        fields = [
            "id",
            "name",
            "image",
            "order",
            "is_active",
        ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            "id",
            "title",
            "number",
            "description",
            "project_link",
            "project_link_text",
            "order",
            "is_active",
        ]


class ExperienceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceSection
        fields = [
            "id",
            "eyebrow",
            "title_light",
            "title_accent",
            "experience_image",
            "is_active",
        ]


class ExperienceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceItem
        fields = [
            "id",
            "year",
            "title",
            "description",
            "order",
            "is_active",
        ]


class TestimonialsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialsSection
        fields = [
            "id",
            "title_light",
            "title_accent",
            "satisfaction_rate",
            "satisfaction_rate_label",
            "repeat_order_rate",
            "repeat_order_label",
            "google_review_rating",
            "google_review_label",
            "hire_button_text",
            "hire_button_link",
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


class ProjectsShowcaseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsShowcaseSection
        fields = [
            "id",
            "eyebrow",
            "title_light",
            "title_accent",
            "max_items",
            "is_active",
        ]


class BlogSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSection
        fields = [
            "id",
            "eyebrow",
            "title_light",
            "title_accent",
            "max_items",
            "is_active",
        ]


class ContactSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        fields = [
            "id",
            "eyebrow",
            "title_light",
            "title_accent",
            "submit_button_text",
            "footer_logo_text",
            "footer_copyright_text",
            "footer_credit_text",
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
    brand_logos = BrandLogoSerializer(many=True)
    skills = SkillSerializer(many=True)
    experience_section = ExperienceSectionSerializer(allow_null=True)
    experience_items = ExperienceItemSerializer(many=True)
    testimonials_section = TestimonialsSectionSerializer(allow_null=True)
    testimonials = TestimonialSerializer(many=True)
    projects_showcase_section = ProjectsShowcaseSectionSerializer(allow_null=True)
    blog_section = BlogSectionSerializer(allow_null=True)
    contact_section = ContactSectionSerializer(allow_null=True)
    social_links = SocialLinkSerializer(many=True)
    contact_info = ContactInfoSerializer(allow_null=True)