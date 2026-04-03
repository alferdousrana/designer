from rest_framework import serializers
from .models import (
    BlogCategory,
    BlogTag,
    BlogPost,
    BlogImage,
    BlogSection,
)


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "order",
            "is_active",
        ]


class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = [
            "id",
            "name",
            "slug",
            "order",
            "is_active",
        ]


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = [
            "id",
            "image",
            "caption",
            "alt_text",
            "order",
            "is_active",
        ]


class BlogSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSection
        fields = [
            "id",
            "title",
            "content",
            "image",
            "order",
            "is_active",
        ]


class BlogPostListSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    tags = BlogTagSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "category",
            "tags",
            "author_name",
            "excerpt",
            "featured_image",
            "cover_image",
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


class BlogPostDetailSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    tags = BlogTagSerializer(many=True, read_only=True)
    gallery = BlogImageSerializer(many=True, read_only=True)
    sections = BlogSectionSerializer(many=True, read_only=True)
    keywords_list = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "category",
            "tags",
            "author_name",
            "excerpt",
            "content",
            "featured_image",
            "cover_image",
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
            "created_at",
            "updated_at",
        ]

    def get_keywords_list(self, obj):
        return obj.get_keywords_list()


class BlogPostWriteSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=BlogCategory.objects.filter(is_active=True),
        source="category",
        write_only=True,
        required=False,
        allow_null=True,
    )
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=BlogTag.objects.filter(is_active=True),
        source="tags",
        many=True,
        write_only=True,
        required=False,
    )

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "category_id",
            "tag_ids",
            "author_name",
            "excerpt",
            "content",
            "featured_image",
            "cover_image",
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
        post = BlogPost.objects.create(**validated_data)
        if tags:
            post.tags.set(tags)
        return post

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if tags is not None:
            instance.tags.set(tags)

        return instance


class BlogCategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "order",
            "is_active",
        ]


class BlogTagWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = [
            "id",
            "name",
            "slug",
            "order",
            "is_active",
        ]


class BlogImageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = [
            "id",
            "post",
            "image",
            "caption",
            "alt_text",
            "order",
            "is_active",
        ]


class BlogSectionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSection
        fields = [
            "id",
            "post",
            "title",
            "content",
            "image",
            "order",
            "is_active",
        ]