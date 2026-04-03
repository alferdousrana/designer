from rest_framework import serializers
from .models import (
    CaseStudy,
    CaseStudyImage,
    CaseStudySection,
    CaseStudyMetric,
)


class CaseStudyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudyImage
        fields = [
            "id",
            "image",
            "caption",
            "alt_text",
            "order",
            "is_active",
        ]


class CaseStudySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudySection
        fields = [
            "id",
            "title",
            "content",
            "image",
            "order",
            "is_active",
        ]


class CaseStudyMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudyMetric
        fields = [
            "id",
            "label",
            "value",
            "order",
            "is_active",
        ]


class CaseStudyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = [
            "id",
            "title",
            "slug",
            "short_desc",
            "thumbnail",
            "cover_image",
            "project_name",
            "client_name",
            "industry",
            "my_role",
            "team",
            "timeline",
            "tools_used",
            "live_url",
            "prototype_url",
            "figma_url",
            "read_time",
            "view_count",
            "keywords",
            "is_featured",
            "is_highlighted",
            "status",
            "published_at",
            "seo_title",
            "seo_description",
            "order",
            "is_active",
            "created_at",
            "updated_at",
        ]


class CaseStudyDetailSerializer(serializers.ModelSerializer):
    gallery = CaseStudyImageSerializer(many=True, read_only=True)
    sections = CaseStudySectionSerializer(many=True, read_only=True)
    metrics = CaseStudyMetricSerializer(many=True, read_only=True)
    tools_list = serializers.SerializerMethodField()
    keywords_list = serializers.SerializerMethodField()

    class Meta:
        model = CaseStudy
        fields = [
            "id",
            "title",
            "slug",
            "short_desc",
            "overview",
            "thumbnail",
            "cover_image",
            "project_name",
            "client_name",
            "industry",
            "my_role",
            "team",
            "timeline",
            "tools_used",
            "tools_list",
            "challenge",
            "goal",
            "process",
            "solution",
            "outcome",
            "live_url",
            "prototype_url",
            "figma_url",
            "read_time",
            "view_count",
            "keywords",
            "keywords_list",
            "is_featured",
            "is_highlighted",
            "status",
            "published_at",
            "seo_title",
            "seo_description",
            "order",
            "is_active",
            "gallery",
            "sections",
            "metrics",
            "created_at",
            "updated_at",
        ]

    def get_tools_list(self, obj):
        return obj.get_tools_list()

    def get_keywords_list(self, obj):
        return obj.get_keywords_list()


class CaseStudyWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = [
            "id",
            "title",
            "slug",
            "short_desc",
            "overview",
            "thumbnail",
            "cover_image",
            "project_name",
            "client_name",
            "industry",
            "my_role",
            "team",
            "timeline",
            "tools_used",
            "challenge",
            "goal",
            "process",
            "solution",
            "outcome",
            "live_url",
            "prototype_url",
            "figma_url",
            "read_time",
            "keywords",
            "is_featured",
            "is_highlighted",
            "status",
            "published_at",
            "seo_title",
            "seo_description",
            "order",
            "is_active",
        ]
        read_only_fields = ["id"]


class CaseStudyImageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudyImage
        fields = [
            "id",
            "case_study",
            "image",
            "caption",
            "alt_text",
            "order",
            "is_active",
        ]


class CaseStudySectionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudySection
        fields = [
            "id",
            "case_study",
            "title",
            "content",
            "image",
            "order",
            "is_active",
        ]


class CaseStudyMetricWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudyMetric
        fields = [
            "id",
            "case_study",
            "label",
            "value",
            "order",
            "is_active",
        ]