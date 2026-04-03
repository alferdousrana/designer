from rest_framework import serializers
from .models import (
    Category,
    ProjectTag,
    Project,
    ProjectImage,
    ProjectSection,
    ProjectMetric,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "order",
            "is_active",
        ]


class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = [
            "id",
            "name",
            "slug",
            "order",
            "is_active",
        ]


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = [
            "id",
            "image",
            "caption",
            "alt_text",
            "order",
            "is_active",
        ]


class ProjectSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSection
        fields = [
            "id",
            "title",
            "content",
            "image",
            "order",
            "is_active",
        ]


class ProjectMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMetric
        fields = [
            "id",
            "label",
            "value",
            "order",
            "is_active",
        ]


class ProjectListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = ProjectTagSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "category",
            "tags",
            "short_desc",
            "thumbnail",
            "cover_image",
            "tools_used",
            "my_role",
            "duration",
            "live_url",
            "behance_url",
            "github_url",
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


class ProjectDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = ProjectTagSerializer(many=True, read_only=True)
    gallery = ProjectImageSerializer(many=True, read_only=True)
    sections = ProjectSectionSerializer(many=True, read_only=True)
    metrics = ProjectMetricSerializer(many=True, read_only=True)
    tools_list = serializers.SerializerMethodField()
    keywords_list = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "category",
            "tags",
            "short_desc",
            "overview",
            "thumbnail",
            "cover_image",
            "tools_used",
            "tools_list",
            "my_role",
            "duration",
            "live_url",
            "behance_url",
            "github_url",
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


class ProjectWriteSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(is_active=True),
        source="category",
        write_only=True,
        required=False,
        allow_null=True,
    )
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=ProjectTag.objects.filter(is_active=True),
        source="tags",
        many=True,
        write_only=True,
        required=False,
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "category_id",
            "tag_ids",
            "short_desc",
            "overview",
            "thumbnail",
            "cover_image",
            "tools_used",
            "my_role",
            "duration",
            "live_url",
            "behance_url",
            "github_url",
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

    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        project = Project.objects.create(**validated_data)
        if tags:
            project.tags.set(tags)
        return project

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if tags is not None:
            instance.tags.set(tags)

        return instance


class CategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "order",
            "is_active",
        ]


class ProjectTagWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = [
            "id",
            "name",
            "slug",
            "order",
            "is_active",
        ]


class ProjectImageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = [
            "id",
            "project",
            "image",
            "caption",
            "alt_text",
            "order",
            "is_active",
        ]


class ProjectSectionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSection
        fields = [
            "id",
            "project",
            "title",
            "content",
            "image",
            "order",
            "is_active",
        ]


class ProjectMetricWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMetric
        fields = [
            "id",
            "project",
            "label",
            "value",
            "order",
            "is_active",
        ]